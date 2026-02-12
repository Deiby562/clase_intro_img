import numpy as np
import matplotlib.pyplot as plt

a = np.array([[0, 0, 0],[25, 255, 25],[50, 50, 50],[75, 255, 75]])
print(a)
print(a.shape)

t=np.array([[0, 0, 0],[255, 25, 255],[255, 50, 255],[255, 75, 255]])
print(t)
print(t.shape)

plt.figure(figsize=(5,5))
plt.imshow(a, cmap='gray', vmin=0, vmax=255)
plt.axis('off')


plt.figure(figsize=(5,5))
plt.imshow(t, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

l = np.array([[255],[255],[255],[255]])

esp_peq = np.ones((1,3))*255


txt_h = np.vstack([a, esp_peq, t])
plt.figure(figsize=(5,9))
plt.imshow(txt_h, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()