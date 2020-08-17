from bs4 import BeautifulSoup
import os
import sys
import re

soup = BeautifulSoup(open(os.path.join(sys.path[0], "hardthings.html"), "r"), 'html.parser')

diluted_soup = soup.find_all(True, {'class':['sectionHeading', 'noteHeading', 'noteText']})

def clean_up_soup(soup_tbc):
	soup_clean = re.sub(r'(.)(\s)(\,|\.|\;|\:|\—|\-|\–|\!|\?)', r'\1\3', soup_tbc)
	soup_clean = re.sub(r'(.)(\s)(\,|\.|\;|\:|\—|\-|\–|\!|\?)', r'\1\3', soup_clean)
	soup_clean = re.sub(r'(\«|\‘|\“|\'|\")(\s)(.)', r'\1\3', soup_clean)
	return soup_clean

def writeNotes(soup):
	# bookTitle = re.sub('\n|\r', '', soup.find(True, {'class':['bookTitle']}).contents[0])
	# bookAuthor = re.sub('\n|\r', '', soup.find(True, {'class':['authors']}).contents[0])

	# print('# ' + bookTitle)
	# print('# ' + bookAuthor + '\n')

	for item in diluted_soup:
		if item['class'][0] == "sectionHeading":
			print('# ' + item.contents[0])
		elif item['class'][0] == 'noteText':
			print('> ' + clean_up_soup(item.string) + '\n')
		elif item['class'][0] == 'noteHeading':
			noteHeadingString = item.get_text(' ', strip=True)
			pages = re.compile(r'(Page [0-9]+)|(Location [0-9]+)')
			pageNumbers = pages.findall(noteHeadingString)
			for i in pageNumbers:
				for e in i:
					print(e)
writeNotes(soup)

