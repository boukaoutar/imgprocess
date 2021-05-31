import cv2
import argparse

try:
    from PIL import Image
except ImportError:
    import Image

#For Making Layer
def convertImage():
    img = Image.open("test.jpg")
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for items in datas:
        #if items[0] == 255 and items[1] == 255 and items[2] == 255:
        newData.append((0, 0, 0, 0))
        #else:
            #newData.append(items)

    img.putdata(newData)
    img.save("layer.png", "PNG")

# now let's initialize the list of reference point
ref_point = []
drawing = False
mode = True

def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ref_point = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))
        if mode == True:
            # draw a rectangle around the region of interest
            v = cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 1)
            cv2.imshow("image", image)

        else:
                cv2.circle(image,(x,y),5,(0,0,255),-1)
                points.append((x,y))
                if len(points)>=2:
                    cv2.line(image,points[-1],points[-2],(0,255,255))

    elif event == cv2.EVENT_RBUTTONDOWN:
        points.clear()


convertImage()

background = Image.open("layer.png")
overlay = Image.open("test.jpg")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.7)
new_img.save("result.png","PNG")

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


# load the image, clone it, and setup the mouse callback function
points = []
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

#layer_1 = cv2.imread("result.png")
#clone_layer = layer_1.copy()
#cv2.namedWindow("layer")
#cv2.setMouseCallback("layer", shape_selection)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('m'):
        mode = not mode

    # press 'r' to reset the window
    elif key == ord("r"):
        image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

cv2.imwrite("finalresult.png",image)

# close all open windows
cv2.destroyAllWindows() 