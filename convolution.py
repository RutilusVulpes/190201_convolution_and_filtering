import numpy as np
import matplotlib.pyplot as plt

img_color = plt.imread('noisy_big_chief.jpeg')
I_gray = img_color.mean(axis=2)
boxcar = np.matrix([[1,1,1],
                   [1,1,1],
                   [1,1,1]])/9

gauss = np.matrix([[1,2,1],
                   [2,4,2],
                   [1,2,1]])/16
def convolve(h,g):

    widthKernal = len(h)
    wBorder = int((widthKernal-1)/2)
    heightKernal = len(h[0])
    hBorder = int((heightKernal-1)/2)

    convolved = np.full((len(g),len(g[0])), 0)

    for i in range(wBorder, len(g)-wBorder-1):
        for j in range(hBorder, len(g[i])-hBorder-1):

            nbhd = np.array([[g[i-1][j-1],g[i-1][j],g[i-1][j+1]],
                             [g[i][j-1],g[i][j],g[i][j+1]],
                             [g[i+1][j-1],g[i+1][j],g[i+1][j+1]]]) @ h

            sum = 0
            for x in np.nditer(nbhd):
                sum = x + sum

            convolved[i][j] = sum
            #print(g[i][j])
    return convolved


I_gray  = convolve(gauss,I_gray)

plt.imshow(I_gray)
plt.show()
