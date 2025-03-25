# Cartoon Image Converter using OpenCV 🖼️🎨

This is a simple Python script that converts an image into a cartoon-style effect using OpenCV.

## Features
- Converts images into a cartoon-like style.
- Uses **adaptive thresholding** for edge detection.
- Applies **bilateral filtering** to smooth colors while preserving edges.
- Outputs a transformed image with a **hand-drawn cartoon effect**.

## Requirements
Make sure you have Python installed along with the required libraries:

## Script Explanation

import cv2
import numpy as np

# Read the image (Change the file name to your image)
img = cv2.imread("mario.png")

# Check if the image is loaded properly
if img is None:
    print("Could not load the image. Please check the file path.")
    exit()

# 1. Convert to grayscale and apply median blur for noise reduction
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# 2. Edge detection using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY,
                              blockSize=11,
                              C=5)

# 3. Apply bilateral filtering to smooth the colors while preserving edges
color = cv2.bilateralFilter(img, d=9,
                            sigmaColor=200,
                            sigmaSpace=200)

# 4. Combine edges and color layers to create the cartoon effect
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Save the cartoonized image
cv2.imwrite("cartoon_output.png", cartoon)

