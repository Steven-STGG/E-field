import csv
import sys
import os


def main():
    if len(sys.argv) !=2:
        sys.exit("Usage: python csv.py CSVfile")
    with open(sys.argv[1],"r",encoding= "utf-8") as f:
        for i in f:
            print (i)

def crawl(directory):
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages