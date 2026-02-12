from utils import img_letra
import matplotlib.pyplot as plt

lt = 'atatatta'
img = img_letra(lt)


for img in imgs_list:
plt.figure(figsize=(5,5))
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()