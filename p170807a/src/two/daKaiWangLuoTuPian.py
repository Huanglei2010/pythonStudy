import urllib.request
from PIL import Image
import io

url = 'http://img5.iqilu.com/c/u/2015/0708/1436362650452.jpg'
file = urllib.request.urlopen(url)
tmpIm = io.BytesIO(file.read())
img = Image.open(tmpIm)
img.show()