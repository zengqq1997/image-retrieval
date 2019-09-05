import cv2
from numpy import shape
import random
import skimage
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
image=mpimg.imread('C:/Users/ZQQ/Desktop/advanced/study/computervision/classtest/image-retrieval/test/21.jpg')
image=skimage.util.random_noise(image, mode='salt', seed=None, clip=True)
plt.figure()
plt.imshow(image)
plt.savefig('test1.jpg')
plt.show()
