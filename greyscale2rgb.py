
# coding: utf-8

# In[1]:


import numpy as np
from PIL import Image
from astropy.io import fits as pyfits


# In[2]:


import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)


# In[3]:


get_ipython().magic('cd greyscale2rgb')


# In[4]:


get_ipython().magic('matplotlib inline')


# In[5]:


get_ipython().magic('ls')


# In[6]:


image_green = Image.open('fc2_save_2019-05-23-094552-0003.jpg')
xsize, ysize = image_green.size
print("Image size: {} x {}".format(xsize, ysize))
plt.imshow(image_green)


# In[7]:


image_red = Image.open('fc2_save_2019-05-23-094552-0004.jpg')
xsize, ysize = image_red.size
print("Image size: {} x {}".format(xsize, ysize))
plt.imshow(image_red)


# In[8]:


green = pyfits.PrimaryHDU(data=image_green)
green.header['LATOBS'] = "32:11:56" # add spurious header info
green.header['LONGOBS'] = "110:56"
green.writeto('green.fits')


# In[ ]:


red = pyfits.PrimaryHDU(data=image_red)
red.header['LATOBS'] = "32:11:56" # add spurious header info
red.header['LONGOBS'] = "110:56"
red.writeto('red.fits')


# In[9]:


image_blue = np.zeros((480,  640))


# In[10]:


image_blue.shape


# In[11]:


blue = pyfits.PrimaryHDU(data=image_blue)
blue.header['LATOBS'] = "32:11:56" # add spurious header info
blue.header['LONGOBS'] = "110:56"
blue.writeto('blue.fits')


# In[12]:


blue.shape


# In[13]:


red.shape


# In[14]:


red_data=pyfits.getdata('red.fits')
green_data=pyfits.getdata('green.fits')
blue_data=pyfits.getdata('blue.fits')


# In[15]:


colorized=np.zeros((red_data.shape[0],green_data.shape[1],3),dtype=int)


# In[16]:


colorized[:,:,0]=red_data; colorized[:,:,1]=green_data; colorized[:,:,2]=blue_data


# In[17]:


plt.imshow(colorized,origin='upper',interpolation='none')
plt.axis('off')
plt.grid(b=None)
plt.show()
plt.clf()


# In[18]:


get_ipython().magic('cd 20190523_rg/')


# In[19]:


get_ipython().magic('ls')


# In[20]:


from pims import ImageSequence


# In[21]:


images = ImageSequence('fc2_save_2019-05-23-094552-*.jpg')


# In[22]:


images


# In[23]:


red_images = images[::2]


# In[24]:


red_images


# In[ ]:


red_images[0]


# In[ ]:


red_images[1]


# In[ ]:


red_images[2]


# In[ ]:


red_images[3]


# In[25]:


green_images = images[1::2]


# In[26]:


green_images


# In[27]:


green_images[0]


# In[ ]:


green_images[1]


# In[28]:


i = 0
for image_green in green_images:
    i = i+1
    green = pyfits.PrimaryHDU(data=image_green)
    green.header['LATOBS'] = "32:11:56" # add spurious header info
    green.header['LONGOBS'] = "110:56"
    green.writeto('{}_green.fits'.format(i))


# In[29]:


i = 0
for image_red in red_images:
    i = i+1
    red = pyfits.PrimaryHDU(data=image_red)
    red.header['LATOBS'] = "32:11:56" # add spurious header info
    red.header['LONGOBS'] = "110:56"
    red.writeto('{}_red.fits'.format(i))


# In[30]:


blue = pyfits.PrimaryHDU(data=image_blue)
blue.header['LATOBS'] = "32:11:56" # add spurious header info
blue.header['LONGOBS'] = "110:56"
blue.writeto('blue.fits')


# In[ ]:


len(images)


# In[31]:


for x in range(2,10):
    print(x)


# In[32]:


rangeMax = len(images)/2


# In[33]:


intRangeMax = int(rangeMax)


# In[34]:


for i in range(1,intRangeMax):
    red_data = pyfits.getdata('{}_red.fits'.format(i))
    green_data = pyfits.getdata('{}_green.fits'.format(i))
    blue_data = pyfits.getdata('blue.fits')
    
    colorized=np.zeros((red_data.shape[0],green_data.shape[1],3),dtype=int)
    colorized[:,:,0]=red_data; colorized[:,:,1]=green_data; colorized[:,:,2]=blue_data
    
    fig = plt.imshow(colorized,origin='upper',interpolation='nearest')
    plt.axis('off')
    plt.grid(b=None)
    
    plt.savefig('colorized_{}.jpeg'.format(i), dpi=100)
        
    plt.show()


# In[ ]:


red_data


# In[ ]:


get_ipython().magic('cd ..')


# In[36]:


## colors reversed: ()


for i in range(1,intRangeMax):
    green_data = pyfits.getdata('{}_red.fits'.format(i)) #here it's nbackwards
    red_data = pyfits.getdata('{}_green.fits'.format(i)) #here it's backwards
    blue_data = pyfits.getdata('blue.fits')
    
    colorized=np.zeros((red_data.shape[0],green_data.shape[1],3),dtype=int)
    colorized[:,:,0]=red_data; colorized[:,:,1]=green_data; colorized[:,:,2]=blue_data
    
    fig = plt.imshow(colorized,origin='upper',interpolation='nearest')
    plt.axis('off')
    plt.grid(b=None)
    
    plt.savefig('flipped_colorized_{}.jpeg'.format(i), dip=300)
        
    plt.show()

