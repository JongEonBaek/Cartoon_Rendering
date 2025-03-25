# Cartoon Effect using OpenCV

## Description
This project applies a cartoon effect to an image using OpenCV. The effect is achieved by performing edge detection and smoothing the color image, then combining the results to create a stylized cartoon-like output.

## Features
- Converts an image to a cartoon-style effect.
- Uses edge detection and adaptive thresholding.
- Applies a bilateral filter to smooth colors while preserving edges.
- Saves the output as an image file.

## Requirements
Make sure you have the following dependencies installed before running the script:

```sh
pip install opencv-python numpy
```

## Usage
1. Place your input image in the same directory as the script.
2. Update the filename in the script (`mario.png`) to match your input image.
3. Run the script:

```sh
python cartoon_effect.py
```

4. The output will be saved as `cartoon_output.png`.

## Code Explanation

```python
import cv2
import numpy as np
```
- Import necessary libraries.

```python
img = cv2.imread("mario.png")
if img is None:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인해주세요.")
    exit()
```
- Load the input image and check if it is loaded properly.

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
```
- Convert the image to grayscale and apply a median blur to reduce noise.

```python
edges = cv2.adaptiveThreshold(gray, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY,
                              blockSize=11,
                              C=5)
```
- Perform adaptive thresholding to detect edges.

```python
color = cv2.bilateralFilter(img, d=9,
                            sigmaColor=200,
                            sigmaSpace=200)
```
- Apply a bilateral filter to smooth colors while keeping edges sharp.

```python
cartoon = cv2.bitwise_and(color, color, mask=edges)
```
- Combine the edge mask with the smoothed color image to create a cartoon effect.

```python
cv2.imwrite("cartoon_output.png", cartoon)
```
- Save the resulting image.

## Example
**Input:**
![Original Image](mario.png)

**Output:**
![Cartoon Effect](cartoon_output.png)

## License
This project is open-source and available under the MIT License.

