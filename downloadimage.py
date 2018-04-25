import os, requests, bs4

os.makedirs('xcdk',exist_ok=True)
url='https://xkcd.com'
num=0
while True:
    if url.endswith('#'):
        print('Download finished')
        break
    else:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        imageElems = soup.select('#comic img')
        if imageElems==[]:
            print("image not found")
        else:
            imageUrl = 'http:' + imageElems[0].get('src')
            imgres = requests.get(imageUrl)
            imgres.raise_for_status()
            imageFile = open(os.path.join('xcdk', os.path.basename(imageUrl)), 'wb')
            for chunk in imgres.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
            num+=1

        prevLink = soup.select('a[rel="prev"]')[0].get('href')
        url = 'http://xkcd.com' + prevLink
print(num)

