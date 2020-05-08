import flickrapi
import os
import urllib.request
from PIL import Image

# Flickr api key 
flickr=flickrapi.FlickrAPI('29487cca09245b19f577b60e1e65c893', '54118c5f8d6f9f34', cache=True)

# parameters
keyword = 'winter landscape'
urlsnumber = 1000
folder = 'winter'

if not os.path.exists(folder):
    os.makedirs(folder)

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=500,          
                     sort='relevance')
					 

for i, photo in enumerate(photos):
    print (i)	

    url = photo.get('url_c')	

    if i > urlsnumber:
        break

    if not url:
        continue
		
    print(url)
    try:
        # Download image from the url 
        urllib.request.urlretrieve(url, folder + "/" + "{:04d}".format(i) +'.jpg')
    except Exception:
        print('Some error happened.')
