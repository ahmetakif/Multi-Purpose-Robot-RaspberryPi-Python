from SimpleCV import *
import time

cam = Camera()
threshold = 5.0

def hareket():
	ilk = cam.getImage()
	time.sleep(0.5)
	son = cam.getImage()
	fark = son - ilk
	matrix = fark.getNumpy()
	mean = matrix.mean()

#	fark.show()

	if mean >= threshold:
		print "hareket algilandi"
		hareket = "e"
	else:
		hareket = "h"

	print 'hareket:', hareket

hareket()

