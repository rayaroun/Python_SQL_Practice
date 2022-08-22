
import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# r = requests.get('https://oshoworld.com/wp-content/uploads/2020/11/Hindi%20Audio/')
# soup = BeautifulSoup(r.content, 'html.parser')

# for a in soup.find_all('a', href=re.compile(r'http.*\.mp3')):
#     print(a)
#     # with open(filename, 'wb') as f:
    
#     #     f.write(doc.content)
#     # break


utl = "https://oshoworld.com/wp-content/uploads/2020/11/Hindi%20Audio/"
r  = requests.get("https://oshoworld.com/wp-content/uploads/2020/11/Hindi%20Audio/")
data = r.text
soup = BeautifulSoup(data)

for i,link in enumerate(soup.find_all('a')):
    
    filename = link.get('href')
    full_url = utl+link.get('href')
    
    if full_url.endswith(".mp3"):
        print(f"{filename} downloading" )
        res = urlopen(full_url)
        # res = urllib2.urlopen(rq)
        mp3 = open("osho/" + filename, 'wb')
        mp3.write(res.read())
        mp3.close()
        print(f"{filename} downloaded" )

    


    if i == 7:
        break