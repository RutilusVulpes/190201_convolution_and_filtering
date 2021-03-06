import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.misc
import math as mt
import imageio as im

img_color = plt.imread('noisy_big_chief.jpeg')
I_gray = img_color.mean(axis=2)
I_gray_copy = img_color.mean(axis=2)
h_box = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
h_gauss = np.array([[1/9,4/9,1/9],[4/9,1/9,4/9],[1/9,4/9,1/9]])
h_sobel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])              

def convolve(g,h): # h is kernel, g is the image
    start = 1
    for i in range(start,len(g[:,1])-1):
        for j in range(start, len(g[i,:])-1):
            f = g[i-1:i+2, j-1:j+2] #FIXME
            total = h*f
            I_gray_copy[i][j] = sum(sum(total)) 
    return I_gray_copy
           
def gauss_kernal(size, var):
    kernel = np.zeros(shape=(size,size))
    for i in range(size):
        for j in range(size):
            kernel[i][j] = mt.exp( -((i - (size-1)/2)**2 + (j - (size-1)/2)**2 )/(2*var*var))
    return kernel           

    
I_gray_copy_box = convolve(I_gray, h_box)
I_gray_copy_gauss = convolve(I_gray, h_gauss)
I_gray_gauss_calc = convolve(I_gray,gauss_kernal(3,.8))
I_gray_sobel = convolve(I_gray,h_sobel)
I_gray_sobel_trans = convolve(I_gray,h_sobel.Transpose())

im.imwrite("box.jpg", I_gray_copy_box)
im.imwrite("gauss_given.jpg", I_gray_copy_gauss)
im.imwrite("gauss_calc.jpg", I_gray_gauss_calc)
im.imwrite("sobel.jpg",I_gray_sobel)
im.imwrite("sobel_trans.jpg",I_gray_sobel_trans)

print( " test.py is done ")

