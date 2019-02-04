import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.misc

img_color = plt.imread('noisy_big_chief.jpeg')
I_gray = img_color.mean(axis=2)

I_gray_copy = img_color.mean(axis=2)

h_box = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

h_gauss = np.array([[1/9,4/9,1/9],[4/9,1/9,4/9],[1/9,4/9,1/9]])
        
        
# g @ h = A 
def convolve(g,h): # h is kernel, g is the image
    t1 = time.clock()
    start = 1
    for i in range(start,len(g[:,1])-1):
        for j in range(start, len(g[i,:])-1):
            f = g[i-1:i+2, j-1:j+2] #FIXME
            
            # need another array to put value into
            total = h*f
       
            I_gray_copy[i][j] = sum(sum(total))
    t2 = time.clock()
    
    print("Time: ", t2-t1)
    
    return I_gray_copy
            # get 3x3 neighborhood of g then multiply it by h
            # call kernel to get the average pixel value and set 
            

    # Return the ave pixel value
I_gray_copy_box = convolve(I_gray, h_box)
I_gray_copy_gauss = convolve(I_gray, h_gauss)

plt.imshow(I_gray_copy_box)
plt.imshow(I_gray_copy_gauss)
plt.show()
scipy.misc.imsave("box.jpg", I_gray_copy_box)
scipy.misc.imsave("gauss.jpg", I_gray_copy_gauss)

#plt.imread(im1)
