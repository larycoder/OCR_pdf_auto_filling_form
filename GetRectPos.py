# import the necessary packages
import cv2
import argparse

# now let's initialize the list of reference point
ref_point = []

def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point, crop, file

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))
        print(str(ref_point))
        file.write(str(ref_point) + '\n')
        # draw a rectangle around the region of interest
        cv2.rectangle(resized, ref_point[0], ref_point[1], (0, 255, 0), 1)
        cv2.imshow("resized", resized)


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-o", "--output", required=True, help="Name of output text file")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
print('Original Dimensions : ',image.shape)
 
scale_percent = 27 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape) 
clone = resized.copy()
cv2.namedWindow("resized")
cv2.setMouseCallback("resized", shape_selection)

file = open(args["output"], 'w')

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("resized", resized)
    key = cv2.waitKey(1) & 0xFF

    # press 'r' to reset the window
    if key == ord("r"):
        image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
file.close()
# close all open windows
cv2.destroyAllWindows() 