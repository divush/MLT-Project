import numpy as np
import cv2


###  Takes input video 
cap = cv2.VideoCapture('here video file')

fourcc = cv2.cv.CV_FOURCC('D','I','V','X')
out = cv2.VideoWriter('Output.AVI',fourcc, 20.0, (640,480),0)  #  change name for each video file here

fgbg = cv2.BackgroundSubtractorMOG2(500,50,bShadowDetection=False)	#history=400,50,0

while(1):
	ret, frame = cap.read()
	#filter frames
	kernel = np.ones((5,5),np.float32)/25
	frame = cv2.filter2D(frame,-1,kernel)
	fgmask = fgbg.apply(frame, learningRate=.005)
	#fill holes
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
	fgmask = cv2.threshold(fgmask, 100, 255, cv2.THRESH_BINARY)[1]
	# print fgmask.shape
	fgmask=cv2.resize(fgmask,(640,480)) 
	out.write(fgmask)              #Output the binary video  

	# cv2.imshow('input',frame)   # showing original video
	cv2.imshow('frame',fgmask)   # showing binary video
	k = cv2.waitKey(30) & 0xff
	if k == 27:
	    break
print "done"
waitKey(0)
cap.release()
cv2.destroyAllWindows()
