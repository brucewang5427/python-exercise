import webbrowser, pyperclip,sys,requests,bs4

if len(sys.argv)>1:
    question=' '.join(sys.argv[1:])
else:
    question=pyperclip.paste()
res=requests.get('https://www.google.com/search?q='+question)
soup=bs4.BeautifulSoup(res.text)
linkElems=soup.select('.r a')
for linkElem in linkElems[:3]:
    webbrowser.open('http://google.com'+linkElem.get('href'))
