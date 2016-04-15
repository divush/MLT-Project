import numpy as np
import os,re
import glob
import cv2
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib


def features(pic):
	kp, des = cv2.SIFT().detectAndCompute(pic, None)
	if des != None:
		y = clf.predict(des)
		temp=[0]*200
		for x in y:
			temp[x-1] = temp[x-1] + 1
		fv.append(temp)
	return des


clf = joblib.load('kmeans_sift.pkl')
test = []
labels=[]




person_limit = 0
person_max_limit = 0
Bicycle_limit = 200
Bicycle_max_limit = 500
Car_limit = 0
Car_max_limit = 0
Motorcycle_limit = 0
Motorcycle_max_limit = 0
Rickshaw_limit = 0
Rickshaw_max_limit = 0
Autorickshaw_limit = 0
Autorickshaw_max_limit = 0
fv=[]
#creating a list of images 
path = "test"
for root, dir_names, file_names in os.walk(path):
# print root, dir_names, file_names
	for name in dir_names:
# print name
		if (name == "Person"):
			for file in os.listdir(path+"/"+name):
				# if person_limit < person_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					pic_des = features(pic)
					if pic_des == None:
						continue
					labels.append(1)
					person_limit+=1
		elif (name == "Bicycle"):
			for file in os.listdir(path+"/"+name):
				# if Bicycle_limit < Bicycle_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					pic_des = features(pic)
					if pic_des == None:
						continue
					labels.append(2)
					Bicycle_limit+=1
		elif (name == "Car"):
			for file in os.listdir(path+"/"+name):
				if Car_limit < Car_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					pic_des = features(pic)
					if pic_des == None:
						continue
					labels.append(3)
					Car_limit+=1
		elif (name == "Motorcycle"):
			for file in os.listdir(path+"/"+name):
				if Motorcycle_limit < Motorcycle_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					pic_des = features(pic)
					if pic_des == None:
						continue
					labels.append(4)
					Motorcycle_limit+=1
		elif (name == "Rickshaw"):
			for file in os.listdir(path+"/"+name):
				if Rickshaw_limit < Rickshaw_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					pic_des = features(pic)
					if pic_des == None:
						continue
					labels.append(5)
					Rickshaw_limit+=1
		elif (name == "Autorickshaw"):
			for file in os.listdir(path+"/"+name):
				if Autorickshaw_limit < Autorickshaw_max_limit :
					pic = cv2.imread(path+"/"+name+"/"+file)
					pic_des = features(pic)
					if pic_des == None:
						continue
					labels.append(6)
					Autorickshaw_limit+=1



svmclf = joblib.load('svm_sift_fine.pkl')
# predlabel=[]
# for vec in fv:
# 	templabel = svmclf.predict(vec)
# 	predlabel.append(templabel)
accuracy = svmclf.score(fv, labels)
print accuracy
