"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from image import Image
import numpy as np
def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    pass
    x_pixels, y_pixels, num_channels = image.array.shape
    # make an empty image so we dont actually modify the original one 
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    #this is the most intuitive way to do this (non-vectorized)
   # for x in range(x_pixels):
    #    for y in range(y_pixels):
     #       for c in range(num_channels):
      #          new_im. array[x, y, c] = image.array[x, y, c] * factor

      # vectorized version
    new_im.array = image.array * factor

    return new_im

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    pass
    x_pixels, y_pixels, num_channels = image.array.shape
    # make an empty image so we dont actually modify the original one 
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid

#vectorized
    new_im.array = ((image.array - mid) * factor) + mid

    return new_im

            

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    pass
    x_pixels, y_pixels, num_channels = image.array.shape
    # make an empty image so we dont actually modify the original one 
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid
    # we are going to use a naive implementation of iterating through each neighbour 
    #and summing 

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    pass

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    pass
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    #lets lighten the lake  
    #brightened_im = brighten(lake, 1.7)
    #brightened_im.write_image('brightened.png') 

#darken
    darkened_im = brighten(lake, 0.3)
    darkened_im.write_image('darkened.jpg')
  # adjust the contrast for the lake 
    incr_contrast = adjust_contrast(lake, 2, 0.5)
    incr_contrast.write_image('increased_contrast.jpg')
    
    # adjust the contrast for the lake 
    decr_contrast = adjust_contrast(lake, 0.5, 0.5)
    decr_contrast.write_image('decreased_contrast.jpg')
    
 