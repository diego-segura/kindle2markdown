import os
import sys
import re

with open('unedited.txt', 'r') as file:
    data = file.read().replace('\n', '')

# this little regex gets most of the spaces
result = re.sub(r'(.)(\s)(\,|\.|\;|\:|\—|\-|\–|\!|\?)', r'\1\3', data)

# this little regex gets spaces in between punctuation and quote marks
result = re.sub(r'(.)(\s)(\,|\.|\;|\:|\—|\-|\–|\!|\?)', r'\1\3', result)

# this little regex gets the spaces at beginning of a quote, i.e. "_ word
result = re.sub(r'(\«|\‘|\“|\'|\")(\s)(.)', r'\1\3', result)

print(data)

print(result)



