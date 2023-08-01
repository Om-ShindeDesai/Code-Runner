# import cv2 library
import cv2

# read the images
img1 = cv2.imread('img_ask.png')
img2 = cv2.imread('img_wer.png')

# vertically concatenates images
# of same width
im_v1 = cv2.vconcat([img1, img2])

# show the output image
cv2.imwrite('res1.png', im_v1)

img3 = cv2.imread('img_hjk.png')
img4 = cv2.imread('img_fdf.png')

# vertically concatenates images
# of same width
im_v2 = cv2.vconcat([img3, img4])

# show the output image
cv2.imwrite('res2.png', im_v2)




# horizontally concatenates images
# of same height
#img5 = cv2.imread('res1.png')
#img6 = cv2.imread('res2.png')
im_h = cv2.hconcat([im_v1, im_v2])

# show the output image
cv2.imwrite('final.png', im_h)
