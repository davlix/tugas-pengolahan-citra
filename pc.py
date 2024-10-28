import numpy as np
import imageio as img
import matplotlib.pyplot as plt

image = img.imread("/Users/davlix/Downloads/images.jpg")

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

imgRed = np.zeros_like(image)
imgGreen = np.zeros_like(image)
imgBlue = np.zeros_like(image)

imgRed[:,:,0] = red  # Red
imgGreen[:,:,1] = green  # Green
imgBlue[:,:,2] = blue  # Blue 

plt.figure(figsize=(10,10))
plt.subplot(4,1,1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(4,1,2)
plt.title("Red Channel")
plt.imshow(imgRed)

plt.subplot(4,1,3)
plt.title("Green Channel")
plt.imshow(imgGreen)

plt.subplot(4,1,4)
plt.title("Blue Channel")
plt.imshow(imgBlue)

plt.tight_layout()
plt.show()
