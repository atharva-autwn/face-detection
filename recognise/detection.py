import cv2
import time

def draw_rect(test_img,face):
    (x,y,w,h) = face
    cv2.rectangle(test_img, (x,y),(x+w,y+h),(0,0,255),thickness=3)

def draw_rect_ready(test_img,face):
    (x,y,w,h) = face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,191,255),thickness=3)

def draw_rect_detect(test_img,face):
    (x,y,w,h) = face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

def put_text(test_img,label_name,x,y):
    cv2.putText(test_img,label_name,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),3)

def distance(x1,y1,x2,y2):
    return (abs(x2-x1)**2 + abs(y2-y1)**2)**0.5

def start():
    flag = 0
    Final_Image = ''
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    while True:
        ret,test_img = capture.read()
        x1 = 200
        y1 = 120
        T = 63
        BA = 250*250
        gray = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,4)
        for face in faces:
            (x,y,w,h) = face
            #print(face, distance(x1,y1,x,y), w*h)
            if distance(x1,y1,x,y) <= T and w*h < 300*300 and w*h > 200*200 :
                draw_rect_detect(test_img,(200,120,250,250))
                put_text(test_img,"Face Detected",x,y)
                Final_Image = test_img
            elif distance(x1,y1,x,y) <= 2*T and w*h < 350*350 and w*h > 150*150 :
                draw_rect_ready(test_img,(200,120,250,250))
                put_text(test_img,"Almost There",x,y)
            else:
                draw_rect(test_img,(200,120,250,250))
                put_text(test_img,"Move your face in the box",x,y)
                
        resized_img = cv2.resize(test_img,(1000,700))
        cv2.imshow('Image',resized_img)
        if cv2.waitKey(1)==ord('q'):
            return Final_Image
    capture.release()
    cv2.destroyAllWindows()
