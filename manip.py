import numpy as np
import cv2

img = cv2.imread("C:\\Users\\Haine\\Desktop\\pythoncode\\cube1.png", cv2.IMREAD_UNCHANGED)

background = cv2.imread("C:\\Users\\Haine\\Desktop\\pythoncode\\testback.png", cv2.IMREAD_UNCHANGED)

rows, cols, dump = img.shape
rows2, cols2, dump2 = background.shape
print(img.shape)
#cube1 = 108, 100, 107

alpha = [0,0,0,0]

def alphabool(first, sec, third):
  if (first >= 108) and (sec <= 100) and (third >= 107):
    return True
  else:
    return False

for i in range(rows):
  for j in range(cols):
    if alphabool(img[i][j][0], img[i][j][1], img[i][j][2]):
      #print("HERE")
      img[i][j] = alpha

d = 1
while int(img.shape[1]) > int(cols/2):
	x_crop = d
	y_crop = 0

	img = img[y_crop:y_crop+img.shape[0], x_crop:x_crop+img.shape[1]]
	filename = "C:\\Users\\Haine\\Desktop\\pythoncode\\cube1(%d).png"%d
	cv2.imwrite(filename, img)

	s_img = cv2.imread(filename, -1)
	print(s_img.shape)

	d += 1
d -= 1
max_y = background.shape[0] - img.shape[0]
temp_d = int(d/2)
while d > temp_d:
	for e in range(0, max_y - 1, 50):
		background = cv2.imread("C:\\Users\\Haine\\Desktop\\pythoncode\\testback.png", cv2.IMREAD_UNCHANGED)
		filename = "C:\\Users\\Haine\\Desktop\\pythoncode\\cube1(%d).png"%d
		print(filename)
		s_img = cv2.imread(filename, -1)
		x_offset = 0
		y_offset = e
		print(s_img.shape)
		y1, y2 = y_offset ,y_offset + s_img.shape[0]
		x1, x2 = x_offset, x_offset + s_img.shape[1]

		alpha_s = s_img[:,:,3]/255.0
		alpha_l = 1.0 - alpha_s

		for c in range(0,3):
		  background[y1:y2, x1:x2, c] = (alpha_s * s_img[:,:,c] + alpha_l * background[y1:y2, x1:x2, c])
		filename2 = "C:\\Users\\Haine\\Desktop\\pythoncode\\cube1back(%d,%d).png"%(d,e)

		cv2.imwrite(filename2, background)
	d -= 1
cv2.waitKey()
