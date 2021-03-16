from bs4 import BeautifulSoup
import requests
source=requests.get('http://example.com/').text
s=BeautifulSoup(source,'html5lib')
#need to install html5lib in your terminal
#i=s.find('article')
#print(i.prettify())
for i in s.find_all('article'):
    h=i.h2.a.text
    try:
        vid_s=i.find('iframe',class_='youtube-player')['src']
        vid_id=vid_s.split("/")[4]
        vid_id=vid_id.split("?")[0]                        
    except Exception as err:
        vid_s="no link"
    print(h)
    yt_link=f"https://youtube.com/watch?v={vid_id}"
    print(yt_link)
    print()