import requests
from bs4 import BeautifulSoup

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
    
