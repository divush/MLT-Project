import numpy as np
import os,re
import glob
import cv2
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

person_limit = 0
person_max_limit = 70
Bicycle_limit = 0
Bicycle_max_limit = 70
Car_limit = 0
Car_max_limit = 70
Motorcycle_limit = 0
Motorcycle_max_limit = 70
Rickshaw_limit = 0
Rickshaw_max_limit = 70
Autorickshaw_limit = 0
Autorickshaw_max_limit = 70
descriptors = np.array([])
#creating a list of images 
path = "Mlt_data"
for root, dir_names, file_names in os.walk(path):
# print root, dir_names, file_names
	for name in dir_names:
		# print name
		if (name == "Person"):
			for file in os.listdir(path+"/"+name):
				if person_limit < person_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					kp, des = cv2.SURF().detectAndCompute(pic, None)
					if des == None:
						continue
					descriptors = np.append(descriptors, des)
					person_limit+=1
					# print path+"/"+name+"/"+file
		elif (name == "Bicycle"):
			for file in os.listdir(path+"/"+name):
				if Bicycle_limit < Bicycle_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					kp, des = cv2.SURF().detectAndCompute(pic, None)
					if des == None:
						continue
					descriptors = np.append(descriptors, des)
					Bicycle_limit+=1
					# print path+"/"+name+"/"+file
		elif (name == "Car"):
			for file in os.listdir(path+"/"+name):
				if Car_limit < Car_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					kp, des = cv2.SURF().detectAndCompute(pic, None)
					if des == None:
						continue
					descriptors = np.append(descriptors, des)
					Car_limit+=1
					# print path+"/"+name+"/"+file
		elif (name == "Motorcycle"):
			for file in os.listdir(path+"/"+name):
				if Motorcycle_limit < Motorcycle_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					kp, des = cv2.SURF().detectAndCompute(pic, None)
					if des == None:
						continue
					descriptors = np.append(descriptors, des)
					Motorcycle_limit+=1
					# print path+"/"+name+"/"+file
		elif (name == "Rickshaw"):
			for file in os.listdir(path+"/"+name):
				if Rickshaw_limit < Rickshaw_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					kp, des = cv2.SURF().detectAndCompute(pic, None)
					if des == None:
						continue
					descriptors = np.append(descriptors, des)
					Rickshaw_limit+=1
					# print path+"/"+name+"/"+file
		elif (name == "Autorickshaw"):
			for file in os.listdir(path+"/"+name):
				if Autorickshaw_limit < Autorickshaw_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					kp, des = cv2.SURF().detectAndCompute(pic, None)
					if des == None:
						continue
					descriptors = np.append(descriptors, des)
					Autorickshaw_limit+=1
					# print path+"/"+name+"/"+file



desc = np.reshape(descriptors, (len(descriptors)/64, 64))
desc = np.float32(desc)
clf = KMeans(n_clusters = 200)
clf.fit(desc)
#dump classifier to file!
joblib.dump(clf, 'kmeans_surf.pkl')
# print "Training Done!"