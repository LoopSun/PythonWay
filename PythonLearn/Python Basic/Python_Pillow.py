#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line

from PIL import Image
img = Image.open('Saturn.jpg')
w, h = img.size
print("Original image size: %s*%s"%(w, h))
img.thumbnail((w/2, h/2))
print("resize image size to: %s*%s"%(w/2, h/2))
img.save('thumbnail.jpg', 'jpg')