import cv2
import numpy as np

# 이미지 읽기 (원하는 이미지 파일 경로로 변경)
img = cv2.imread("mario.png")

# 이미지가 제대로 로드되었는지 확인
if img is None:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인해주세요.")
    exit()

# 1. 그레이스케일로 변환 후, 노이즈 제거를 위해 중간 블러 적용
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# 2. 에지 검출: adaptiveThreshold를 이용하여 에지(윤곽선) 검출
edges = cv2.adaptiveThreshold(gray, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY,
                              blockSize=11,
                              C=5)

# 3. 컬러 이미지를 부드럽게 하기 위해 bilateral filter 적용 (색상은 유지하면서 노이즈 제거)
color = cv2.bilateralFilter(img, d=9,
                            sigmaColor=200,
                            sigmaSpace=200)

# 4. 에지와 컬러 이미지를 결합하여 만화 효과 적용
cartoon = cv2.bitwise_and(color, color, mask=edges)

# 결과 이미지를 파일로 저장 (원하는 파일명으로 변경 가능)
cv2.imwrite("cartoon_output.png", cartoon)
