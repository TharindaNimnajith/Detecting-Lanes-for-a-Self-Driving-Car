from PIL import ImageGrab  #used for capturing the pc screen/window
import cv2
import numpy as np

def crop(image):
    p1 = [0, 225]
    p2 = [220, 60]
    p3 = [450, 60]
    p4 = [650, 225]

    points = np.array([p1, p2, p3, p4])
    
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [points], 255)

    cropped = cv2.bitwise_and(image, mask) 
    cropped[150:240, 250:400] = [0]
    
    #cv2.imshow('CROP', cropped)
    return cropped
    
x1, y1, x2, y2 = 10, 150, 660, 460

while(True):
    window = ImageGrab.grab(bbox = (x1, y1, x2, y2))
    windowArray = np.array(window)
    
    windowRGB = cv2.cvtColor(windowArray, cv2.COLOR_BGR2RGB)
    windowGRAY = cv2.cvtColor(windowRGB, cv2.COLOR_BGR2GRAY)
    #windowGRAY1 = cv2.cvtColor(windowRGB, cv2.COLOR_RGB2GRAY)
    
    edges = cv2.Canny(windowGRAY, threshold1 = 200, threshold2 = 300)
    cropped = crop(edges)
    
    #cv2.imshow('LIVE', windowArray)
    #cv2.imshow('LIVE', windowRGB)
    #cv2.imshow('LIVE', windowGRAY)
    #cv2.imshow('LIVE1', windowGRAY1)
    #cv2.imshow('LIVE', edges)
    cv2.imshow('LIVE', cropped)
    
    cv2.waitKey(1)
