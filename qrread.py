#!/usr/bin/python

from sys import argv
import zbar
import Image


# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
pil = Image.open("base.png").convert('L')
width, height = pil.size
raw = pil.tostring()

# wrap image data
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
del(image)

