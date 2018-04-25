import urllib.request as re, lxml.html
def download(url,user_agent='Socrates',num=2):
    print('Downloading '+url)
    headers={'user_agent':user_agent}
    request=re.Request(url,headers=headers)
    try:
        html=re.urlopen(request).read()
    except re.URLError as e:
        print('Download Failed '+e.reason)
    return html

try:
    html=download('https://xkcd.com/965/')
    tree=lxml.html.fromstring(html)
    img=tree.xpath('//img/@src')
    x=0
    for i in img:
        re.urlretrieve('https://xkcd.com'+i,'%s.jpg'%x)
        x+=1
except Exception as e:
    print(e)