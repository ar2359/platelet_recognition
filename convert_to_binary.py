#convert image to binary

import cv2
import numpy as np
from time import sleep
import scipy.ndimage as ndi
import glob

count_img=1
file1 = open("labels.txt","w")


for imag in glob.glob("C:\\Path to images\\*.tif"): #change extension accordingly


	img=cv2.imread(imag)
	img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

	#OTSU Thresholding
	ret,thr =cv2.threshold(img,0,255,cv2.THRESH_OTSU)
	
	m,n=thr.shape
	thr2=thr.copy()


	#filling holes



	hello,contours, hier = cv2.findContours(thr,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

	count=0;
	for cnt in contours:
		if cv2.contourArea(cnt)<80 and cv2.contourArea(cnt)>20:
		#if cv2.contourArea(cnt)>20:
			count=count+1
			cv2.drawContours(img,[cnt],0,(0,255,0),2)
			cv2.drawContours(thr,[cnt],0,255,-1)
			
	#print(count)




	#cv2.imwrite('D:\\Anirudh\\Python\\Mini_Project\\Pics\\bw.jpg',thr)
	plate = np.zeros(shape=(m,n))

	for i in range(0,m):
		for j in range(0,n):
			if thr2[i][j]==thr[i][j]:
				plate[i][j]=255
			else:
				plate[i][j]=thr2[i][j]
				
				

	#cv2.imwrite('D:\\Anirudh\\Python\\Mini_Project\\Pics\\only_platelets.jpg',plate)
	#plate = cv2.bitwise_not(plate)

	for i in range(0,m):
		for j in range(0,n):
			if plate[i][j]==0:
				plate[i][j]=255
			else:
				plate[i][j]=0

	#cv2.imshow('hello',plate)
	#cv2.waitKey(0)



	labeled_array, num_features = ndi.label(plate)
	#print(num_features)

	st='C:\\Users\\anirudhsr\\Desktop\\Demo\\blood'+str(count_img)+'.png'
	
	

	
	cv2.imwrite(st,plate)
	
	
	#file1.write(st+ ' ' + str(num_features)+'\n')
	
	
	#print(count_img)
	count_img=count_img+1
	print(num_features)
	
	
	
file1.close()

#Convert image into grayscale
#Use OTSU thresholding to convert it into black and white
#Use contour plots to cover up all the platelets
#Extract only the platelets from the original black&white image (find the difference between the two images)
#invert the black and white image to obtain white platelets on a black background
#Find clusters of 1's in the black&white image to obtain the number of platelets in the given image
#Multiply the number obtained by a scalar to obtain a projected count of the number of platelets




