
# coding: utf-8

# In[2]:


import cv2
import csv


# In[5]:


with open('images/train_labels.csv') as f:
    r = csv.reader(f)
    next(r, None)
    for row in r:
        img = cv2.imread('images/' + row[0])
        crop_img = img[int(row[5]):int(row[7]), int(row[4]):int(row[6])]
        cv2.imwrite('images/img_crop/{}'.format(row[0]), crop_img)


# In[4]:


img

