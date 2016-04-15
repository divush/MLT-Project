# this files takes the input as video and the corresponding json file and den crop the image in corresponding label folder .

import cv2
import json

def get_frames(fname, frame_count):
    frames = [[] for _ in range(frame_count)]
    with open(fname) as json_data:
        data = json.load(json_data)
        for _,item in data.iteritems():
            for fno,inst in item["boxes"].iteritems():
                inst['label'] = item['label']
                frames[int(fno)].append(inst)
    return frames


cap = cv2.VideoCapture('here video file')
fcount = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
frames = get_frames('here corresponding json file', int(fcount))

Person_count = 0
Car_count = 0
Bicycle_count = 0
Motorcycle_count = 0
Autorickshaw_count = 0
Rickshaw_count = 0
Number_Plate_count = 0
success,image = cap.read()
i = 0
while(success):
	for j in range(0 , len(frames[i])):
		if frames[i][j]['label']=='Person' and frames[i][j]['occluded']==0 and frames[i][j]['outside']==0:
			# img = cv2.imread("frame%d.jpg" % count)
			crop_img = image[frames[i][j]['ytl']:frames[i][j]['ybr'], frames[i][j]['xtl']:frames[i][j]['xbr']] # Crop from x, y, w, h -> 100, 200, 300, 400
			# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
			# cv2.imshow("cropped", crop_img)
			cv2.imwrite("Mlt_data/Person/Person6_%d.jpg" % Person_count, crop_img)    #  make folder
			Person_count+=1
			# cv2.imwrite("cropped.jpg", crop_img)
			cv2.waitKey(0)
		elif frames[i][j]['label']=='Car' and frames[i][j]['occluded']==0 and frames[i][j]['outside']==0:
			crop_img = image[frames[i][j]['ytl']:frames[i][j]['ybr'], frames[i][j]['xtl']:frames[i][j]['xbr']] # Crop from x, y, w, h -> 100, 200, 300, 400
			cv2.imwrite("Mlt_data/Car/Car6_%d.jpg" % Car_count, crop_img)           #  make folder
			Car_count+=1
			cv2.waitKey(0)
		elif frames[i][j]['label']=='Bicycle' and frames[i][j]['occluded']==0 and frames[i][j]['outside']==0:
			crop_img = image[frames[i][j]['ytl']:frames[i][j]['ybr'], frames[i][j]['xtl']:frames[i][j]['xbr']] # Crop from x, y, w, h -> 100, 200, 300, 400
			cv2.imwrite("Mlt_data/Bicycle/Bicycle6_%d.jpg" % Bicycle_count, crop_img)                #  make folder
			Bicycle_count+=1
			cv2.waitKey(0)
		elif frames[i][j]['label']=='Motorcycle' and frames[i][j]['occluded']==0 and frames[i][j]['outside']==0:
			crop_img = image[frames[i][j]['ytl']:frames[i][j]['ybr'], frames[i][j]['xtl']:frames[i][j]['xbr']] # Crop from x, y, w, h -> 100, 200, 300, 400
			cv2.imwrite("Mlt_data/Motorcycle/Motorcycle6_%d.jpg" % Motorcycle_count, crop_img)           #  make folder
			Motorcycle_count+=1
			cv2.waitKey(0)
		elif frames[i][j]['label']=='Autorickshaw' and frames[i][j]['occluded']==0 and frames[i][j]['outside']==0:
			crop_img = image[frames[i][j]['ytl']:frames[i][j]['ybr'], frames[i][j]['xtl']:frames[i][j]['xbr']] # Crop from x, y, w, h -> 100, 200, 300, 400
			cv2.imwrite("Mlt_data/Autorickshaw/Autorickshaw6_%d.jpg" % Autorickshaw_count, crop_img)           #  make folder
			Autorickshaw_count+=1
			cv2.waitKey(0)
		elif frames[i][j]['label']=='Rickshaw' and frames[i][j]['occluded']==0 and frames[i][j]['outside']==0:
			crop_img = image[frames[i][j]['ytl']:frames[i][j]['ybr'], frames[i][j]['xtl']:frames[i][j]['xbr']] # Crop from x, y, w, h -> 100, 200, 300, 400
			cv2.imwrite("Mlt_data/Rickshaw/Rickshaw6_%d.jpg" % Rickshaw_count, crop_img)            #  make folder
			Rickshaw_count+=1
			cv2.waitKey(0)
		elif frames[i][j]['label']=='Number_Plate' and frames[i][j]['occluded']==0 and frames[i][j]['outside']==0:
			crop_img = image[frames[i][j]['ytl']:frames[i][j]['ybr'], frames[i][j]['xtl']:frames[i][j]['xbr']] # Crop from x, y, w, h -> 100, 200, 300, 400
			cv2.imwrite("Mlt_data/Number_Plate/Number_Plate6_%d.jpg" % Number_Plate_count, crop_img)              #  make folder
			Number_Plate_count+=1
			cv2.waitKey(0)
	for d in range(0,10):
		success,image = cap.read()
		i+=1