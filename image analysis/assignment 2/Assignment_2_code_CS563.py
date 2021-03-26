import cv2
import numpy as np

inputname = input("Enter the file name : ")
print(' ')
print(' ')
image = cv2.imread(inputname, -1)

print("use the numbers assigned below for each filter ")
print("1. histogram stretching")
print("2. gamma correction")
print("3. median filter")
take = str(input("Enter the sequence of filters you want to apply on the image ( ex: 3 1 2 ):  "))
li= take.split(" ")

def stackImages(scale,imgArray): # This function is for the purpose of stacking images side by side for easy comparision
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0].shape[1]
    height = imgArray[0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def histogramStretching(image): # function to perform histogram stretching
    # Shape of image
    m, n = image.shape

    # Create copy of image
    new_image = np.zeros((m, n), np.uint8)

    # Calculate minimum value in image
    min = image.min()

    # Calculate difference between min and max value in image
    val = image.max() - image.min()
    for rows in range(image.shape[0]):
        for columns in range(image.shape[1]):
            new_image[rows][columns] = ((image[rows][columns] - min) / val) * 255

    return new_image

# giving different gamma values for different images
if inputname=='Building.pgm':
    gammaValue = 0.3
if inputname=='MRI.pgm':
    gammaValue = 1.7
if inputname=='peppers.pgm':
    gammaValue = 0.8

def gammaCorrection(image, gamma): # function to perform power law transformation on the image
    corrected = 255 * (image / 255) ** (1.0 / gamma)
    corrected = corrected.astype(np.uint8)
    return corrected


def medianFilter(image):# function to apply median filter
    # Shape of image
    m, n = image.shape

    # Create a dummy image
    median = np.zeros((m, n), np.uint8)
    for i in range(1, m - 3):
        for j in range(1, n - 3):
            temp = image[i - 1: i + 2, j - 1: j + 2]
            temp = temp.flatten()
            temp.sort()
            median[i][j] = temp[4]

    return median
ans=[image]
for key,i in enumerate(li):
    if i=='1':
        k = histogramStretching(ans[key])
        ans.append(k)
    if i=='2':
        k = gammaCorrection(ans[key],gammaValue)
        ans.append(k)
    if i=='3':
        k = medianFilter(ans[key])
        ans.append(k)
stacked = stackImages(1,[image,ans[-1]])
cv2.imshow('original image(a)     after_applying_filters(b)',stacked)
print(' ')
print(' ')
print('============= PART - 2 =====================')
image1 = ans[-1]
m, n = image1.shape
img_filter_copy_x = image1.copy()
img_filter_copy_y = image1.copy()
print(' ')
print(' ')

print("use the numbers assigned below for each edge detector ")
print("1. detecting edges using prewitt mask ")
print("2. detecting edges using sobell mask")
print("3. detecting edges using central difference")

edge_det = input("Enter the edge detector you want to apply ( ex: 3 ):  ")

def applyedgedetector(img1,i,j,m,n): # performing edge detection
    if i + 3 <= m and j + 3 <= n:
        middle_row = int(i + 1)
        middle_column = int(j + 1)
        if middle_row < m and middle_column < n:
            sum = np.sum(np.sum(img1[i:i + 3, j:j + 3] * kernelx))
            sum_y = np.sum(np.sum(img1[i:i + 3, j:j + 3] * kernely))
            if sum>60:
                img_filter_copy_x[middle_row, middle_column] = 255
            else :
                img_filter_copy_x[middle_row, middle_column] = 0
            if sum_y>60:
                img_filter_copy_y[middle_row, middle_column] = 255
            else:
                img_filter_copy_y[middle_row, middle_column] = 0


def applyFiltering():
     for i in range(m):
         for j in range(n):
             applyedgedetector(image1, i, j, m, n)


if edge_det == '1':
    # prewitt kernel
    kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    name = 'prewitt'
    applyFiltering()

if edge_det == '2':
    # sobel kernel
    kernelx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    kernely = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
    name = 'sobel'
    applyFiltering()

if edge_det == '3':
    # center difference kernel
    kernelx = np.array([[-0.5],[0],[0.5]])
    kernely = np.array([-0.5,0,0.5])
    name = 'centered_diff'
    applyFiltering()


# cv2.imshow("Image1", image1)
# cv2.imshow(name, img_filter_copy_x+img_filter_copy_y)
# cv2.imshow(name+"_Vertical", img_filter_copy_y)
# cv2.imshow(name+"_horizontal", img_filter_copy_x)
stacked = stackImages(1,[image1,img_filter_copy_x+img_filter_copy_y])
cv2.imshow('after applying filters(a)       detected edges using mask (b)',stacked)
cv2.waitKey(0)