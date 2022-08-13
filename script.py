import re

import requests
from bs4 import BeautifulSoup

CLEANR = re.compile('<.*?>')

# download webpage (don't tell Parson)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
url = 'https://s1.sos.mo.gov/candidatesonweb/DisplayCandidatesPlacement.aspx?ElectionCode=750005605' 
r = requests.get(url=url, headers=headers, stream=True)

filename = 'temp.html'
# write file to dir
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
# parse it using beautifulsoup
with open(filename, 'r') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# each section is an h3; find each and add to list
header_list = soup.find_all('h3')
cleaned_header_list = []

for h in header_list:
    cleaned_header_list.append(str(h))

rep_table_list = []
dem_table_list = []
for ch in cleaned_header_list:
    # find the header in the document
    header = soup.find(string=ch)
    # once the first header is established (and stored?), get the next item, which should be the first table.
    first_table = header.find_next('table') 
    # add header to rep_table_list, if it's republican

    # once you get the first table, you can get the second... if there is one.
    
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext
