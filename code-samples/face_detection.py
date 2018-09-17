import cv2
 
scale_factor = 1.2
min_neighbors = 3
min_size = (50, 50)
webcam=True #if working with video file then make it 'False'
 
def detect(path):
 
    cascade = cv2.CascadeClassifier(path)
    if webcam:
        video_cap = cv2.VideoCapture(0) # use 0,1,2..depanding on your webcam
    else:
        video_cap = cv2.VideoCapture("videoFile.mp4")
    while True:
        # Capture frame-by-frame
        ret, img = video_cap.read()
 
        #converting to gray image for faster video processing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
        rects = cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                         minSize=min_size)
        # if at least 1 face detected
        if len(rects) >= 0:
            # Draw a rectangle around the faces
            for (x, y, w, h) in rects:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
            # Display the resulting frame
            cv2.imshow('Face Detection on Video', img)
            #wait for 'c' to close the application
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break
    video_cap.release()
 
def main():
    cascadeFilePath="haarcascade_frontalface_alt.xml"
    detect(cascadeFilePath)
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()