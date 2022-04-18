import cv2
import numpy as np
import matplotlib.pyplot as plt

# import image containing qr code
qr_code_img = cv2.imread('img/qrcode.png')

# convert from BGR to RGB
rgb_qrcode = cv2.cvtColor(qr_code_img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb_qrcode', rgb_qrcode)
cv2.waitKey(0) 
#closing all open windows 
cv2.destroyAllWindows() 

# detect where qr code is on the image
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(qr_code_img)

if bbox is not None:
    print('QR detected')
# obtain the coordinates of the four corners of the qr code
print(bbox)

# outline where qrcode is on image by putting rectangular border around it
qrcode_copy = rgb_qrcode.copy()
plt.figure(figsize = (10,8))
cv2.rectangle(qrcode_copy, (372,241), (488,126), (0,0,255), 6)
cv2.imshow('qrcode', qrcode_copy)
cv2.waitKey(0) 
#closing all open windows 
cv2.destroyAllWindows() 

#crop the image to only show qrcode
qrcode_cropped = qrcode_copy[126:241, 372:488]
cv2.imshow('qrcode_cropped', qrcode_cropped)
cv2.waitKey(0) 
#closing all open windows 
cv2.destroyAllWindows() 

#save cropped image containing just the qr code
cv2.imwrite('img/qrcode_cropped.png',qrcode_cropped)
