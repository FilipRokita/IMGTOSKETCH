#IMGTOSKETCH
#Filip Rokita
#www.filiprokita.com

import cv2

inputImage = input("FULL INPUT IMAGE NAME(MUST BE IN SCRIPT DIRECTORY): ")

image = cv2.imread(inputImage)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invertedGray = 255 - gray
blurredInvertedGray = cv2.GaussianBlur(invertedGray, (21, 21), 0)
invertedBlurredInvertedGray = 255 - blurredInvertedGray
sketch = cv2.divide(gray, invertedBlurredInvertedGray, scale=256.0)

sketchName="IMGTOSKETCH-"+inputImage
cv2.imwrite(sketchName, sketch)

print("DONE")