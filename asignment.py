#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import numpy as np
import matplotlib.pylab as plt
from PIL import Image

def plti(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')
    

pics = []


mainArray = np.zeros(shape=(150,150,3))

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        pics.append(fname)

print(pics)


for name in pics:
    get_ipython().run_line_magic('matplotlib', 'inline')
    try:
        img = Image.open(mohsin1)
        if img.format == "JPEG":
            im = plt.imread(mohsin1)
            im = im[:150,:150,:3]
          
            mainArray += im
            print("length of single picture:",len(im), "||  Shape of this picture: ",im.shape)
    except:
        print("not supported file")
    
print("\nProcess comleted with the size of array: ")
print("Size of main array containing all the images: ",len(mainArray))


# In[ ]:





# In[ ]:




