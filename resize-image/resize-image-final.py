# Import OpenCV
import cv2
import get_screen_information

screen_height = (get_screen_information.screen_height)
screen_width = (get_screen_information.screen_width)

# Open the image
img = cv2.imread('brian.jpg', 1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get image size
img.shape
height, width, channel = img.shape


# Resize the image: Downscalling
img_down = cv2.resize(img, (width//3, height//3))
cv2.imshow('smaller image', img_down)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize the image: Upscalling
img_up = cv2.resize(img_down, (width, height), interpolation = cv2.INTER_LINEAR)
cv2.imshow('bigger image', img_up)
cv2.waitKey(0)
cv2.destroyAllWindows()