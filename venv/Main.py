import os
import cv2
import random
import math
import pickle
import time
import numpy as np
from sklearn.decomposition import PCA
from sklearn import svm

def designAlgorithm (gamma, components):
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    
    trainingSplit = .75
    #n_components = 30
    n_components = components

    root_dir = './Faces'
    
    #This is just to differentiate the control faces which have a value of 0
    # , to the actual allowed users
    y_value = 0
    y_holder = 1

    for directory, subdirectories, files in os.walk(root_dir):
        if "s0" in directory:
            y_value = 0
        elif "/s" in directory:
            y_value = y_holder
            y_holder = y_holder + 1

        images = []
        for file in files:
            #For some reason, MacOS generated these files in the folder
            if "DS_Store" not in file:
                #Load each image, resize if it isnt part of the 
                #original photo dataset, then grayscale each of them
                
                img = cv2.imread(os.path.join(directory, file))
                if y_value > 0:
                    img = cv2.resize(img, (250,250))
                
                img = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
                if len(images) != 0:
                    indexLocation = random.randint(0, len(images)) % len(images)
                else:
                    indexLocation = 0
                #after randomizing the index, insert the img into the temp images array
                images.insert(indexLocation, img)
        
        #Seperate training set from testing set
        split = math.floor(len(images)*trainingSplit)
        count = 0
        for img in images:
            if (count < split):
                if len(X_train) != 0:
                    indexLocation = random.randint(0, len(X_train)) % len(X_train)
                else:
                    indexLocation = 0

                X_train.insert(indexLocation, img)
                y_train.insert(indexLocation, y_value)
            else:
                if len(X_test) != 0:
                    indexLocation = random.randint(0, len(X_test)) % len(X_test)
                else:
                    indexLocation = 0

                X_test.insert(indexLocation, img)
                y_test.insert(indexLocation, y_value)
                
            count = count + 1

    # Converting arrays to numpy arrays
    # Obtaining the dimensionality from these arrays
    # Then reshaping the arrays to allow us to fit to the PCA algorithm
    X_train = np.array(X_train)
    nsamples, h, w = X_train.shape
    X_train = X_train.reshape((nsamples, h*w))

    X_test = np.array(X_test)
    nsamples, h, w = X_test.shape
    X_test = X_test.reshape((nsamples, h*w))

    pca = PCA(n_components=n_components, whiten=True, svd_solver='randomized').fit(X_train)

    eigenfaces = pca.components_.reshape((n_components, h, w))

    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)

    C=1.0
    #clf = svm.SVC(kernel='rbf', gamma=1, C=C)
    clf = svm.SVC(kernel='rbf', gamma=gamma, C=C)
    clf.fit(X_train_pca, y_train)


    y_pred = clf.predict(X_test_pca)

    score = 0.0
    for i in range(len(y_test)):
        print("Expected:"+str(y_test[i])+" Prediction:"+str(y_pred[i]))
        if (y_test[i] == y_pred[i]):
            score += 1
        elif (y_test[i] > 0 and y_pred[i] == 0):
            score +=.5
        


    # with open('./algoSave', 'wb') as f:
    #     pickle.dump(clf, f)
    # with open('./pca', 'wb') as f:
    #     pickle.dump(pca, f)
    return score

def defineUser(img):
    X = []
    clf = pickle.load(open('./algoSave', 'rb'))
    pca = pickle.load(open('./pca', 'rb'))

    img = cv2.resize(img, (250,250))
    img = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
    X.append(img)
    
    X = np.array(X)
    nsamples, h, w = X.shape
    X = X.reshape((nsamples, h*w))
    
    X_pca = pca.transform(X)
    predictedValue = clf.predict(X_pca)

    if (predictedValue > 0):
        print("Authorized User")
    else:
        print("Unauthorized User")


def detect(path):
    scale_factor = 1.2
    min_neighbors = 3
    min_size = (50, 50)
 
    cascade = cv2.CascadeClassifier(path)
    video_cap = cv2.VideoCapture(0) # use 0,1,2..depanding on your webcam
    
    while True:
        # Capture frame-by-frame
        ret, img = video_cap.read()
        gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
        rects = cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                         minSize=min_size)
        if len(rects) >= 0:
            cv2.imshow('Face Detection on Video', img)

            if cv2.waitKey(1) & 0xFF == ord('c'):
                defineUser(img)
                break
    video_cap.release()
 
def liveCamera():
    cascadeFilePath="./lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_alt.xml"
    detect(cascadeFilePath)
    cv2.destroyAllWindows()

#gamma = 0.01
#n_components = 40

max_score = 0.0
perfect_pairs = []

for gamma in range(1, 1000, 1):
    for components in range(1, 40):
        score = designAlgorithm (gamma/100, components)  
        if (score == 30):
            perfect_pairs.append((gamma/100,components))
        if (score > max_score):
            max_score = score


for i in perfect_pairs:
    print(i)

print(max_score)

#designAlgorithm()
#liveCamera()