"""
A python script to generate ASCII image of a normal jpeg image.
"""

import cv2
import numpy

# Function to take rgb tuple average
def compute(arr):
    sum = 0
    for i in arr:
        sum += i
    
    return sum//3


def create(val):

    char_sequence = """`^\",:;Il!i ~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""

    temp = val//25

    return char_sequence[temp]


if __name__ == "__main__":

    # Reading the image
    img = cv2.imread('PATH OF THE IMAGE',0)

    k = 25

    width = int((img.shape[1])/k)
    height = int((img.shape[0])/k)


    scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
   


    image_2dArray = numpy.array(scaled)    # Creating the 2d array of tuple of rgb values of the pixels

   
    ascii_arr = []

    # the ASCII image
    for i in image_2dArray:
        temp_arr = []
        for j in i:
            temp_arr.append(create(j))

        ascii_arr.append(temp_arr)


    
    
    with open("image.txt",'w') as file:
        for i in ascii_arr:
            for j in i:
                file.write(j*2)
            file.write('\n')
  
