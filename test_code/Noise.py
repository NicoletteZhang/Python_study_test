# -*- coding:utf-8 -*-
import cv2
import numpy as np

# 读取图片
img = cv2.imread("zxp.jpg", cv2.IMREAD_UNCHANGED)
img_noise = img

cv2.imshow("src", img)

rows, cols, chn = img_noise.shape

# 加噪声
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img_noise[x, y, :] = 255

cv2.imshow("noise", img_noise)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存含噪声图像
cv2.imwrite("zxp_noise.jpg", img_noise)