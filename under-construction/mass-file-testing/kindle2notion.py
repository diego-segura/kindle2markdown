#!/usr/bin/python3

from bs4 import BeautifulSoup
import os
import sys
import re

def clean_up_soup(soup_clean):
    soup_clean = re.sub(r'(.)(\s)(\,|\.|\;|\:|\—|\-|\–|\!|\?)', r'\1\3', soup_clean)
    soup_clean = re.sub(r'(.)(\s)(\,|\.|\;|\:|\—|\-|\–|\!|\?)', r'\1\3', soup_clean)
    soup_clean = re.sub(r'(\«|\‘|\“|\'|\")(\s)(.)', r'\1\3', soup_clean)
    return soup_clean

def writeNotes(diluted_soup):
    notebook = open((bookTitle + '.md'),"a")
    for item in diluted_soup:
        if item['class'][0] == "sectionHeading":
            notebook.write('# ' + item.contents[0] + '\n')
        elif (item['class'][0] == 'noteText') and item.string:
            print(item.string)
            notebook.write('> ' + clean_up_soup(item.string) + '\n\n—\n\n')
        elif item['class'][0] == 'noteHeading':
            noteHeadingString = item.get_text(' ', strip=True)
            # notebook.write(noteHeadingString)
            pages = re.compile(r'Page [0-9]+|Location [0-9]+')
            # notebook.write(pages)
            pageNumbers = pages.findall(noteHeadingString)
            # notebook.write(pageNumbers)
            notebook.write(' - '.join(pageNumbers) + '\n\n')

for filename in os.listdir():
    if filename.endswith(".html"): 
        soup = BeautifulSoup(open(os.path.join(sys.path[0], filename), "r"), 'html.parser')
        bookTitle = re.sub('\n|\r', '', soup.find(True, {'class':['bookTitle']}).contents[0])
        diluted_soup = soup.find_all(True, {'class':['sectionHeading', 'noteHeading', 'noteText']})
        writeNotes(diluted_soup)
        continue
    else:
        continue
