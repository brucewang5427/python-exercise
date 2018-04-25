import requests, bs4, sys, os, pyperclip,random
from selenium import webdriver

browser=webdriver.Chrome()
os.makedirs('linkdownload',exist_ok=True)
if len(sys.argv)>1:
    inputurl=sys.argv[1]
else:
    inputurl=pyperclip.paste()

browser.get(inputurl)
linkElems=browser.find_elements_by_tag_name('a')
if linkElems==[]:
    print('No link found')
else:
    for linkElm in linkElems:
        #linkElm.click()
        browser.execute_script("arguments[0].click();",linkElm)
        browser.implicitly_wait(100)
        currenturl=browser.current_url
        res=requests.get(currenturl)
        #soup=bs4.BeautifulSoup(res.text)
        try:
            linkFile=open(os.path.join('linkdownload',random.randint(1,1000000000)),'wb')
            for chunk in res.iter_content(100000):
                linkFile.write(chunk)
            linkFile.close()
        except Exception as ex:
            print(ex)
print('Done')
