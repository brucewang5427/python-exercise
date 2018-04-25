import requests,os,bs4,threading
os.makedirs('multidownload',exist_ok=True)
def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        print('Downloading page http://xkcd.com/%s...'%urlNumber)
        res=requests.get('http://xkcd.com/%s'%urlNumber)
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text)
        comicElem=soup.select('#comic img')
        if comicElem==[]:
            print('Could not find comic image')
        else:
            comicUrl='http:'+comicElem[0].get('src')
            print('Downloading image %s...'%comicUrl)
            res=requests.get(comicUrl)
            res.raise_for_status()
            imgFile=open(os.path.join('multidownload',os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close()

downloadThreads=[]
for i in range(0,160,16):
    downloadThread=threading.Thread(target=downloadXkcd,args=(i,i+15))
    downloadThreads.append(downloadThread)
    downloadThread.start()
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done')