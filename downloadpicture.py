import webbrowser, bs4, requests,os,sys, pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if len(sys.argv)>1:
    searchinput=sys.argv[1:]
else:searchinput=pyperclip.paste()

url='http://flickr.com'
os.mkdir('flickr')
browser=webdriver.Chrome()
browser.get(url)
inputElm=browser.find_element_by_id('search-field')
inputElm.send_keys(searchinput)
inputElm.submit()
currentrul=browser.current_url
res=requests.get(currentrul)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
imgElms=soup.select('div[class="view photo-list-photo-view requiredToShowOnServer awake"]')
if imgElms==[]:
    print('No picture found')
else:
   for imgElm in imgElms:
       try:

           imgStyle=imgElm.get('style')
           styles=imgStyle.split(';')
           bckgrds=[x for x in styles if 'url' in x]
           urls=bckgrds[0].split('(')
           url=urls[1]
           imgUrl='http:'+url[:-1]
           imgRes=requests.get(imgUrl)
       except Exception as ex:
           print(ex)
       imgRes.raise_for_status()

       imgFile=open(os.path.join('flickr',os.path.basename(imgUrl)),'wb')
       for chunk in imgRes.iter_content(100000):
           imgFile.write(chunk)
       imgFile.close()

"""
while not url.endswith('#'):
    print('Downloading page %s...'%url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)

    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('can not found the image')
    else:
        comicUrl='http:'+comicElem[0].get('src')
        print('Downloading image %s...'%(comicUrl))
        res=requests.get(comicUrl)
        res.raise_for_status()

        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    preLink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+preLink.get('href')
print('done')
"""