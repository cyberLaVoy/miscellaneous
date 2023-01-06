
import cv2
import numpy as np
import matplotlib.pyplot as plt

def displayImage(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imagesIntro():
    #img = cv2.imread("hibiscus.jpg", cv2.IMREAD_GRAYSCALE)
    # or
    img = cv2.imread("hibiscus.jpg", 0)
    # IMREAD_GRAYSCALE = 0
    # IMREAD_COLOR = 1
    # IMREAD_UNCHANGED = -1

    cv2.imshow("hibiscus", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # for writing modified image in current directory
    #cv2.imwrite("hibiscus(greyscale).png", img)

    """
    plt.imshow(img, cmap="gray", interpolation="bicubic")
    plt.show()
    """

def videosIntro():
    # to capture webcam 0, 1, 2, ...
    #cap = cv2.VideoCapture(0)

    cap = cv2.VideoCapture("random.mp4")
    #fourcc = cv2.VideoWriter_fourcc(*"XVID")
    #out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #out.write(gray)

        cv2.imshow("Frame", frame)
        cv2.imshow("Modified Frame", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    #out.release()
    cv2.destroyAllWindows()

def imageOperations():
    img = cv2.imread("hibiscus.jpg", cv2.IMREAD_COLOR)
    # get pixel color value
    pixel = img[300,350]
    # modify pixel color value
    img[300,350] = [255, 255, 255]
    x = 25
    y = 0
    img[y,x] = [255, 255, 255]
    # get region of image
    roi = img[0:50, 0:50]
    # modify region of image
    x1 = 25
    y1 = 25
    x2 = 100
    y2 = 100
    img[y1:y2, x1:x2] = [0,0,0]

    # find center of image
    height = len(img)
    width = len(img[0])
    center = (width//2, height//2)

    # copy and paste region of image
    roi = img[280:340, 330:390]
    img[273:333, 100:160] = roi

    # black out center of image
    w = 50
    h = 50
    x1 = center[0] - w//2
    y1 = center[1] - h//2
    x2 = x1 + w
    y2 = y1 + h
    img[y1:y2, x1:x2] = [0,0,0]

    # white out center pixel
    img[center[1], center[0]] = [255,255,255] # img[y,x] = [255,255, 255]

    cv2.imshow("Hibiscus", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imageArithmeticAndLogic():
    img1 = cv2.imread("iceberg.jpg")
    img1 = img1[50:550, 50:550]
    img2 = cv2.imread("wildfire.jpg")
    img2 = img2[50:550, 50:550]
    img3 = cv2.imread("small-flower.jpg")

    # adding images together
    # added = img1 + img2
    # added = cv2.add(img1,img2)
    # added = cv2.addWeighted(img1, .6, img2, .4, 0)

    img4 = cv2.addWeighted(img1, .6, img2, .4, 0)
    # paste an image on top of another
    rows,cols,channels = img3.shape
    roi = img4[0:rows, 0:cols]
    img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img3gray, 210, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)
    img4_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img3_fg = cv2.bitwise_and(img3,img3, mask=mask)
    dst = cv2.add(img4_bg, img3_fg)
    img4[0:rows, 0:cols] = dst

    displayImage("Final Image", img4)

def thresholding():
    img = cv2.imread("bookpage.jpg")
    #retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
    gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)

    # retval3,threshold3 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
    displayImage("Image", gauss)

def colorFiltering():
    img = cv2.imread("red-flowers.jpg")    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hsv hue sat value
    lower_red = np.array([100,50,50])
    upper_red = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(img, img, mask=mask)

    # blurring an image
    kernal = np.ones((15,15), np.float32)/(15*15)
    smoothed = cv2.filter2D(res, -1, kernal)
    blur = cv2.GaussianBlur(res, (5,5), 0)
    median = cv2.medianBlur(res, 5)
    bilateral = cv2.bilateralFilter(res, 15, 75, 57)

    # morphological transformations
    kernal = np.ones((3,3), np.uint8)
    # remove an outlying color in a group of pixels
    erosion = cv2.erode(mask, kernal, iterations = 1)
    # expand an outlying color in a group of pixels
    dilation = cv2.dilate(mask, kernal, iterations = 6)

    kernal = np.ones((10,10), np.uint8)
    # remove false positives
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
    # remove false negatives
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

    res = cv2.bitwise_and(img, img, mask=dilation)

    displayImage("Filterd", res)

def gradient(fileName):
    img = cv2.imread(fileName)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    displayImage("Gradient", laplacian)
    displayImage("Gradient", sobelx)
    displayImage("Gradient", sobely)

def edgeDetection(fileName):
    img = cv2.imread(fileName)
    edges = cv2.Canny(img, 75, 75)
    edges_inv = cv2.bitwise_not(edges)
    displayImage("Edges", edges_inv)

# could be used for character recognition?
def cornerDetection(fileName):
    img = cv2.imread(fileName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray) # to satisfy the corner detection algorithm
                                    # image, maxCorners, qualityLevel, minDistance
    corners = cv2.goodFeaturesToTrack(gray, 1000, .01, 1)
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)
    displayImage("Corners", img)

def main():
    # note: colors are in bgr, not rgb
    # note: .png is a good file type choice (non-lossy, still allows some compression)
    #       avoid .jpg for 2 reasons: 1. lossy compression, 2. compression artifacts
    #imagesIntro()
    #videosIntro()
    #imageOperations()
    #imageArithmeticAndLogic()
    #thresholding()
    #colorFiltering()
    #gradient("iceberg.jpg")
    #edgeDetection("street.jpg")
    #edgeDetection("sudoku-original.jpg")
    cornerDetection("sudoku-original.jpg")

if __name__ == "__main__":
    main()