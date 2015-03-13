"""
Name: Terrence Johnson
Date:2/10/15
CST 205/Section 2
"""

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageChops
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os


def ela (pix, filename):
	"""
	    Implementation of error level anaylsis. The idea is not mine. You can read about it here.
		
		http://blackhat.com/presentations/bh-dc-08/Krawetz/Whitepaper/bh-dc-08-krawetz-WP.pdf
			http://resources.infosecinstitute.com/error-level-analysis-detect-image-manipulation/ """
	temp = pix
	
	newCopy = filename + '.new.jpg'
	temp.save(newCopy, 'JPEG', quality=95)
	compare = Image.open(newCopy)
	temp = ImageChops.difference(temp, compare)
	ext = temp.getextrema()
	diff = max([ex[1] for ex in ext])
	scale = 255.0/diff
	temp = ImageEnhance.Brightness(temp).enhance(scale)
	
	temp.show()
	if os.path.exists(newCopy):
		os.remove(newCopy)
	return 
	


def imageData (pix):
	"""
		This function uses PIL.Exiftags to print exif data in english
	"""
	import PIL.ExifTags
	
	if pix._getexif() is None:
		return
	
	for k,v in pix._getexif().items():
		print(PIL.ExifTags.TAGS[k], v)
	
	return
	

print("Select the JPEG you want to manipulate")
Tk().withdraw()
filename=askopenfilename()

print ("Your file location is: " + filename) 

pix = Image.open(filename)

pix.show()

ela(pix, filename)

imageData(pix)