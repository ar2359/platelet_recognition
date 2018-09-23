import numpy as np
import cv2
from imgaug import augmenters as iaa
import imgaug as ia
import imutils
import glob

count=1

for imag in glob.glob("D:\\Path to images\\*.png"):

	st='D:\\Destination path for Augmented set\\Augmented Set\\image_name_prefix'

	img = cv2.imread(imag,-1)


	flipper = iaa.Fliplr(1.0)

	flipperud=iaa.Flipud(1.0)
	
	pt=iaa.PerspectiveTransform(scale=(0.05, 0.05))

	 
	
	for angle in np.arange(0, 270, 90):
		rotated = imutils.rotate(img, angle)
		#cv2.imshow("Rotated (Problematic)", rotated)
		#cv2.waitKey(0)
	 
	
	for angle in np.arange(0, 270, 90):
		rotated = imutils.rotate_bound(img, angle)
		cv2.imwrite(st+str(count)+'.png',img)
		count=count+1
		
		imp1=pt.augment_image(img)
		cv2.imwrite(st+str(count)+'.png',imp1)
		count=count+1
		
		img2=flipper.augment_image(img)
		cv2.imwrite(st+str(count)+'.png',img2)
		count=count+1
		
		imp2=pt.augment_image(img2)
		cv2.imwrite(st+str(count)+'.png',imp2)
		count=count+1
		
		img3=flipperud.augment_image(img)
		cv2.imwrite(st+str(count)+'.png',img3)
		count=count+1
		
		imp3=pt.augment_image(img3)
		cv2.imwrite(st+str(count)+'.png',imp3)
		count=count+1
		
		
		
	
