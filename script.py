import re

import requests
from bs4 import BeautifulSoup

CLEANR = re.compile('<.*?>')

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

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
    cleaned_header_list.append(cleanhtml(str(h)))

rep_count = 0
dem_count = 0
for ch in cleaned_header_list:
    # find the header in the document
    header = soup.find(string=ch)
    # once the first header is established (and stored?), get the next item, which should be the first table.
    first_table = header.find_next('table') 
    # add header to rep_table_list, if it's republican
    first_table_caption = cleanhtml(str(first_table.find_next('caption')))
    breakpoint()
    if first_table_caption == "Republican":
        rep_count += 1
    elif first_table_caption == "Democratic":
        dem_count += 1

    second_table = first_table.find_next('table')
    second_table_caption = cleanhtml(str(first_table.find_next('caption')))
    breakpoint()
    if second_table_caption == "Republican":
        rep_count += 1
    elif second_table_caption == "Democratic":
        dem_count += 1
    # once you get the first table, you can get the second... if there is one.
    
print(f"There are {len(header_list)} primary elections happening in Missouri in 2022")
print(f"There are {rep_count} Republican tickets in these elections")
print(f"There are {dem_count} Democratic tickets in these elections")
    
