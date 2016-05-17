#!/usr/bin/env python

import cv2.cv as cv 
import time 

cv.NamedWindow('camera',1)

capture = cv.CaptureFromCAM(0)

while  True:
	img = cv.QueryFrame(capture)

	cv.SaveImage('test1.jpg',img)


	if cv.WaitKey(10) == 27:
		break

cv.DestroyAllWindows()