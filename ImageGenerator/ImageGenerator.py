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
    img = cv2.imread('C:/Users/Harivansh Thakur/Desktop/mario.jpg',0)

    # height, width, color = img.shape

    k = 25

    width = int((img.shape[1])/k)
    height = int((img.shape[0])/k)

    # print(height,width)

    scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    # cv2.imshow("hello",scaled)
    # cv2.waitKey(0)


    image_2dArray = numpy.array(scaled)    # Creating the 2d array of tuple of rgb values of the pixels

    # print(image_2dArray[100][10])
    # making single value array

    # Pixel_Array = []

    # for i in image_2dArray:
    #     temp = []
    #     for j in i:
    #         temp.append(compute(j))
    #     Pixel_Array.append(temp)

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



    # for i in ascii_arr:
    #     for j in i:
    #         print(j*2,end="")
    #     print() 
    
    



