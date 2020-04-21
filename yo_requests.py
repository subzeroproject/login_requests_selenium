import requests
import urllib
from lxml import html
from bs4 import BeautifulSoup

with requests.Session() as T:
    url = "https://cm.litextension.com/login"

    headers = {
        'Origin' : 'https://cm.litextension.com',
        'Referer' : 'https://cm.litextension.com/login',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36'


        }
#lấy url , token và login
    page = T.get(url)
    soup = BeautifulSoup(page.content , 'html.parser')
    token = soup.select_one('input[name = "_token"]')['value']
    login = { 'email': 'test1@test.com','password':'aA123456', '_token' : token}
    r = T.post(url , login , headers)
    ok = r.content
    #print(ok)

#in profile user
    url2 = "https://cm.litextension.com/profile"
    page2 = T.get(url2)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    html2 = soup2.get_text()
    #print(html2)
    takehtml = html.fromstring(page2.content)
    info = takehtml.xpath('//*[@id="profile"]/div[1]/div[1]/div')
    print(info)

    
    
