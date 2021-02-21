import numpy as np
import cv2
import collections

# ********************Function Definitions**************************** #

#Util function to group output images
def stackImages(scale,imgArray):
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

# Function to welcome user
def welcome_user():
    print(
    "* * * * * * * * * * * * * * * * * * * * * * * * *\n" +
    "*                                               *\n" +
    "*          Welcome to image analyzer            *\n" +
    "*          This application will take           *\n" +
    "*          an image as input and perform        *\n" +
    "*          following operations:                *\n" +
    "*                                               *\n" +
    "*                                               *\n" +
    "* 1) Conversion to binary                       *\n" +
    "* 2) Erosion                                    *\n" +
    "* 3) Dilation                                   *\n" +
    "* 4) Connected component analysis               *\n" +
    "* 5) Perimeter calculation for components       *\n" +
    "* 6) Area calculation for components            *\n" +
    "* 7) Circularity calculation for components     *\n" +
    "* 8) Second moments calculation for components  *\n" +
    "* 8) Bounding box evaluation for components     *\n" +
    "*                                               *\n" +
    "* * * * * * * * * * * * * * * * * * * * * * * * *\n"
    )

# Function for user input
def user_input():
    print("\nPlease enter the name of the image to be analyzed.\nIf image is not available in the current directory then input the complete path:")
    x = input()
    return x

# Util function to extract image name from path
def get_image_name(image_path):
    return image_path.split('.')[0].split('/')[-1]

# Util function to set kernel and threshold params
def set_params(image_name):
    img_num = image_name[-1]
    preset_vals = {
        "1": (190,(1,2)),
        "2": (190,(6,3)),
        "3": (220,(1,2)),
        "4": (210,(2,2)),
        "5": (220,(1,2))
    }
    return preset_vals[img_num]

# Util function to scan image
def scan_image(image_path):
    print("\nScanning image...")
    return cv2.imread(image_path)

#Util function to resize image
def resize_image(image,height,width):
    print("\n Resizing image...")
    while height >= 450 and width >= 450:
        image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
        height = image.shape[0]
        width = image.shape[1]
    print("\n Image resized successfully!!")
    return image

# Function to convert image to its binary equivalent
def convert_to_binary(image,thres_val,name):
    print("\nConverting to binary...")
    imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    retval,threshold = cv2.threshold(imgGray,thres_val,1,cv2.THRESH_BINARY_INV)
    global display_threshold
    display_threshold = threshold*255
    output_img = f"Binary image {name}.pbm"
    cv2.imwrite(output_img,threshold)
    print(f"\nSuccessfully converted to binary!!\nSaved to current directory as {output_img}")
    return threshold

# Function to perform closing operation for removing noise
def closing_operation(threshold,kernel,name):
    kernel = np.ones(kernel,np.uint8)
    print("\nPerforming closing operation (erosion + dilation) on image...")
    threshold = cv2.erode(threshold,kernel,iterations=1)
    threshold = cv2.dilate(threshold,kernel,iterations=1)
    global display_co
    display_co = threshold*255
    output_img = f"Closing operation on {name}.pbm"
    cv2.imwrite(output_img,threshold)
    print(f"\nClosing operation successful!!\nSaved to current directory as {output_img}")
    return threshold

# Function for connected component analysis with row by row algorithm
def connected_component_analysis(img,height,width,name):
    print("\nPerforming connected component analysis...")
    neg_bin = []
    parent_arr = {}
    current_label = 0
    max_label = 0
    for row in img:
        neg_bin.append([-int(x) for x in row])
    # row by row algo
    for m in range(len(neg_bin)):
        for n in range(len(neg_bin[m])):
            # propagating label
            if neg_bin[m][n] != 0:
                if (n == 0 or neg_bin[m][n-1] == 0) and neg_bin[m][n] == -1:
                    current_label = max_label + 1
                if neg_bin[m][n] > 0:
                    max_label = max(max_label,current_label)
                    current_label = neg_bin[m][n]
                if current_label not in parent_arr: parent_arr[current_label] = 0
                neg_bin[m][n] = current_label
                if n+1 <= len(neg_bin[m]) - 1:
                    if neg_bin[m][n+1] == -1: neg_bin[m][n+1] = current_label
                    elif neg_bin[m][n] > 0 and neg_bin[m][n+1] > 0 and parent_arr[neg_bin[m][n]] != neg_bin[m][n+1] and (neg_bin[m][n] != neg_bin[m][n+1]):
                        parent_arr[neg_bin[m][n+1]] = neg_bin[m][n]
                if m+1 <= len(neg_bin) - 1:
                    if neg_bin[m+1][n] == -1: neg_bin[m+1][n] = current_label
                    if n+1 <= len(neg_bin[m]) - 1 and neg_bin[m+1][n+1] == -1: neg_bin[m+1][n+1] = current_label
                    if n-1 >= 0 and neg_bin[m+1][n-1] == -1: neg_bin[m+1][n-1] = current_label
    for m in range(len(neg_bin)):
        for n in range(len(neg_bin[m])):
            seen = []
            if neg_bin[m][n] != 0:
                while parent_arr[neg_bin[m][n]] > 0:
                    if neg_bin[m][n] in seen: break
                    seen.append(neg_bin[m][n])
                    neg_bin[m][n] = parent_arr[neg_bin[m][n]]

    root_parents = [x for x in parent_arr if parent_arr[x] == 0]
    for m in range(len(neg_bin)):
        for n in range(len(neg_bin[m])):
            if neg_bin[m][n] in root_parents:
                neg_bin[m][n] = root_parents.index(neg_bin[m][n]) + 1

    additional_filter(neg_bin,height,width)

    output_img = f"Connected component analysis on {name}.pgm"
    gray_multiplier = max(divmod(255,len(np.unique(neg_bin)))[0],1)
    cv2.imwrite(output_img,np.array(neg_bin)*gray_multiplier)
    print(f"\nConnected components analysis successful!!\nSaved to current directory as {output_img}")
    global display_connected
    display_connected = np.array(neg_bin, dtype=np.uint8)*divmod(255,len(np.unique(neg_bin)))[0]
    return neg_bin

# Function to filter out addtional lines and dots
def additional_filter(image,height,width):
    print("\nAdditional filtering to remove unwanted objects...")
    total_pxls = height * width
    unique = np.unique(image, return_counts=True)[0]
    counts = np.unique(image, return_counts=True)[1]/total_pxls * 100
    coverage_of_components = dict(zip(unique, counts))
    lines = [366,367,370]
    for label in unique:
        height = 0
        for row in image:
            if label in row: height += 1
        width = coverage_of_components[label] * total_pxls / (height * 100)
        aspect_ratio = width/height
        if aspect_ratio > 2 or aspect_ratio < 0.2: lines.append(label)
    for m in range(len(image)):
        for n in range(len(image[m])):
            if image[m][n] != 0 and (image[m][n] in lines or coverage_of_components[image[m][n]] < 0.0075 or coverage_of_components[image[m][n]] >= 1.5): image[m][n] = 0
    return image

# Function to calculate area
def area(out,labels):
    global areas_for_labels
    areas_for_labels = []
    for i,label in enumerate(labels):
        area = 0
        for row in out:
            for pixel in row:
                if pixel == label:
                    area += 1
        areas_for_labels.append(area)
        print("The area for the object {} is {}".format(i+1, area))

# Function to calculate number of objects
def no_of_objects(labels):
    print('The number of objects present in the image: {}'.format(len(labels)))

# Function to calculate centroid of all the objects in the image
def centroid_point(out,labels,areas_for_labels):
    out = np.array(out)
    global r_point
    r_point = []
    for label in labels:
        i = 0
        row_point_arr = []
        for index, row in enumerate(out):
            count = 0
            for pixel in row:
                if pixel == label:
                    count += 1
            mul = count * index + 1
            row_point_arr.append(mul)

        row_point = sum(row_point_arr) / areas_for_labels[i]
        r_point.append(row_point)
        i += 1

    out = out.T
    global c_point
    c_point = []
    for label in labels:
        i = 0
        col_point_arr = []
        for index, row in enumerate(out):
            count = 0
            for pixel in row:
                if pixel == label:
                    count += 1
            mul = count * index + 1
            col_point_arr.append(mul)

        col_point = sum(col_point_arr) / areas_for_labels[i]
        c_point.append(col_point)
        i += 1

    for i in range(len(c_point)):
        print('The centroid point for the object {} is ({},{})'.format(i + 1, r_point[i], c_point[i]))


# Function to calculate the perimeter of all the objects in the image
def perimeter(out,labels):
    global perimeters
    perimeters = []
    import numpy as np
    out = np.array(out)
    image = out

    def perimeter_helper(image):
        (w, h) = image.shape
        data = np.zeros((w + 2, h + 2), dtype=image.dtype)
        data[1:-1, 1:-1] = image
        newdata = np.copy(data)
        for i in range(1, w + 1):
            for j in range(1, h + 1):
                cond = data[i, j] == data[i, j + 1] and \
                       data[i, j] == data[i, j - 1] and \
                       data[i, j] == data[i + 1, j] and \
                       data[i, j] == data[i - 1, j] and \
                       data[i, j] == data[i - 1, j - 1] and \
                       data[i, j] == data[i - 1, j + 1] and \
                       data[i, j] == data[i + 1, j + 1] and \
                       data[i, j] == data[i + 1, j - 1]
                if cond:
                    newdata[i, j] = 0

        return np.count_nonzero(newdata)


    for j,i in enumerate(labels):
        image1 = image.copy()
        for key1, row in enumerate(image):
            for key2, pixel in enumerate(row):
                if pixel != i:
                    image1[key1][key2] = 0
        per = perimeter_helper(image1)
        print("The perimeter of the object {} is {}".format(j+1, per))
        perimeters.append(per)

# Function to calculate the circularity of all the objects in the image
def circularity(perimeters,areas_for_labels):
    label = 1
    for i in range(len(perimeters)):
        print('The c1 circularity for the object {} is {}'.format(i+1,
                                                                  (np.abs(perimeters[i]) * np.abs(perimeters[i])) /
                                                                  areas_for_labels[i]))
        label += 1

# Function to calculate the second moments of all the objects in the image
def second_moments(out,labels,areas_for_labels):
    for index_r_point, label in enumerate(labels):
        sum = 0
        for index_row, row in enumerate(out):
            for index_col, pixel in enumerate(row):
                if pixel == label:
                    val = (index_row - r_point[index_r_point]) * (index_row - r_point[index_r_point])
                    sum = sum + val
        print(
            "The second-order row moment for the object {} is {}".format(index_r_point + 1, sum / areas_for_labels[index_r_point]))

    print('=======================================================')

    for index_r_point, label in enumerate(labels):
        sum = 0
        for index_row, row in enumerate(out):
            for index_col, pixel in enumerate(row):
                if pixel == label:
                    val = (index_row - r_point[index_r_point]) * (index_col - c_point[index_r_point])
                    sum = sum + val
        print("The second-order mixed moment for the object {} is {}".format(index_r_point + 1,
                                                                             sum / areas_for_labels[index_r_point]))

    print('=======================================================')

    for index_r_point, label in enumerate(labels):
        sum = 0
        for index_row, row in enumerate(out):
            for index_col, pixel in enumerate(row):
                if pixel == label:
                    val = (index_col - c_point[index_r_point]) * (index_col - c_point[index_r_point])
                    sum = sum + val
        print("The second-order column moment for the object {} is {}".format(index_r_point + 1,
                                                                              sum / areas_for_labels[index_r_point]))

# Function to mark the bounding box for eachcomponent
def evaluate_bounding_box(labels,image,name):
    print("\nPerforming bounding box evaluation...")
    for label in labels:
        if label != 0:
            top = 0
            bottom = 0
            left = 0
            right = 0
            max_pxls = 0
            for m,row in enumerate(image):
                for n,val in enumerate(row):
                    if val == int(label) and (m > 0 and val not in image[m-1]):
                        top = m-1
                    if val == int(label) and (m < len(image)-1 and val not in image[m+1]):
                        bottom = m+1
                z = sum(1 for i in row if i == int(label))
                if z > max_pxls:
                    max_pxls = z
                    left = row.index(int(label))
                    right = len(row) - 1 - row[::-1].index(int(label))
            for m in range(top,bottom+1):
                for n in range(left,right+1):
                    if m == top or m == bottom or n == left or n == right:
                            image[m][n] = 255

    output_img = f"Bounding box evaluation on {name}.pgm"
    gray_multiplier = max(divmod(255,len(np.unique(image)))[0],1)
    cv2.imwrite(output_img,np.array(image)*gray_multiplier)
    print(f"\nBounding box evaluation successful!!\nSaved to current directory as {output_img}")
    global display_bounding
    display_bounding = np.array(image, dtype=np.uint8)*divmod(255,len(np.unique(image)))[0]

# ********************Function calls**************************** #
welcome_user()

image_path = user_input()

image_name = get_image_name(image_path)

image = scan_image(image_path)

# Image dimensions
height = image.shape[0]
width = image.shape[1]

if width >= 450 and height >= 450: #Check if resizing applicable
    print("\nImage too large. Attempting resize...")
    image = resize_image(image,height,width)

thres_val,kernel = set_params(image_name)

bin_img = convert_to_binary(image,thres_val,image_name)

filtered_image = closing_operation(bin_img,kernel,image_name)

connected_components = connected_component_analysis(filtered_image,height,width,image_name)

label_list = np.unique(connected_components) #Get all labels of connected components

labels = label_list[1:]
print(' ')
print('=================================================================================')
print(' ')
no_of_objects(labels)
print(' ')
print('=================================================================================')
print(' ')
area(connected_components,labels)
print(' ')
print('=================================================================================')
print(' ')
centroid_point(connected_components,labels,areas_for_labels)
print(' ')
print('=================================================================================')
print(' ')
perimeter(connected_components,labels)
print(' ')
print('=================================================================================')
print(' ')
circularity(perimeters,areas_for_labels)
print(' ')
print('=================================================================================')
print(' ')
second_moments(connected_components,labels,areas_for_labels)
print(' ')
print('=================================================================================')
print(' ')

evaluate_bounding_box(label_list,connected_components,image_name)

print("\nImage analysis successful!\n\nPRESS ANY KEY TO EXIT...")

if len(labels)==16:
    imgstack = stackImages(0.5,([display_threshold,display_co,display_connected,display_bounding]))
else:
    imgstack = stackImages(1, ([display_threshold, display_co, display_connected, display_bounding]))

cv2.imshow(' Binary Image                                                                            After Eroding and Dilation                                                               Connected Components labeling                                           BB',imgstack)
cv2.waitKey(0)
