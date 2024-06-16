
#Importing Library
import cv2
import os
#Load Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image_path="images/face1.jpg" # must change whit your path
if not(os.path.exists(image_path)):
    print("Image not found")
    exit()

#Load image
our_image_color = cv2.imread(image_path)
our_image_gray = cv2.cvtColor(our_image_color,cv2.COLOR_RGB2GRAY)

#Detect face
faces = face_cascade.detectMultiScale(our_image_gray,
scaleFactor = 1.05,minNeighbors = 8)
#1.05 8
if len(faces) > 0:
    #Draw a rectangle around face
    for x, y, w, h in faces:
        our_image_rect = cv2.rectangle(our_image_color, (x,y), (x+w,y+h), (150,255,0), 2)
    # Show Image
    cv2.imshow("Face Detection", our_image_rect)
    print("number of faces that i can found is :"+str(faces.shape[0]))
else:
    cv2.imshow("Face Detection", our_image_color)
    print("i cant found any faces")

cv2.waitKey(0)
cv2.destroyAllWindows