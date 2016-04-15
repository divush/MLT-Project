import numpy as np
import cv2
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

clf = joblib.load('../kmeans_surf.pkl')
treeclf = joblib.load('svm_surf_fine_rbf_100.pkl')  # chnage name accordingly 

def features(pic):
	kp, des = cv2.SURF().detectAndCompute(pic, None)
	if des != None:
		y = clf.predict(des)
		temp=[0]*200
		for x in y:
			temp[x-1] = temp[x-1] + 1
		return temp
	return None
Person_count=0
cap1 = cv2.VideoCapture('give binary video as input .AVI')    # takes binary image
cap2 = cv2.VideoCapture('corresponding original video .mov')   # corresponding original video
labels = {1:"Person", 2:"Bicycle", 3:"$-wheeler", 4:"Motorcycle",5:"Rickshaw",6:"autoRickshaw"}

fgbg = cv2.BackgroundSubtractorMOG2(400,50,bShadowDetection=False)	#history=400,50,0
while(1):
	ret1, frame1 = cap1.read()
	ret2, frame2 = cap2.read()
	if frame2!=None:
		frame2=cv2.resize(frame2,(640,480)) 
	else:
		continue
	imgray = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,127,255,0)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

	areas = [cv2.contourArea(c) for c in contours]
	for index in range(0,len(areas)):
		
		if areas[index] > 500:
			cnt=contours[index]
			x,y,w,h = cv2.boundingRect(cnt)

			cv2.rectangle(frame2,(x,y),(x+w ,y+h),(0,255,0),2)
			cv2.rectangle(frame1,(x,y),(x+w ,y+h),(0,255,0),2)
			crop_img = frame2[y:y+h, x:x+w]
			pic_fv = features(crop_img)
			if pic_fv==None:
				continue
			img_label = treeclf.predict(pic_fv)
			my_str = labels[img_label[0]]
			cv2.putText(frame2, my_str, (x+w/2,y+h/2), cv2.FONT_HERSHEY_PLAIN, 2.0, color=(0,0,255),thickness=2)
			print img_label
		

	cv2.imshow('input',frame2)
	# cv2.imshow('frame',frame1)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
	    break

cap.release()
cv2.destroyAllWindows()