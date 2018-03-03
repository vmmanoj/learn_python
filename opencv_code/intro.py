import numpy as np
import cv2

# Based on: https://docs.opencv.org/3.3.1/dc/d2e/tutorial_py_image_display.html

# Reading Image from file
img = cv2.imread('../data/sample_img.JPG')

# Displaying Image
cv2.imshow('image',img)

# Waiting for Input KeyStroke
cv2.waitKey(0)

# Writing to Output Image
cv2.imwrite('../data/output/output_img.png', img)

# Cleaning Up Windows and Exiting
cv2.destroyAllWindows()
