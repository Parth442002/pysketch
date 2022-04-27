import cv2
import matplotlib.pyplot as plt


def sketch(img_path):
    img = cv2.imread(img_path)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey_img)
    blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)
    invblur_img = cv2.bitwise_not(blur_img)
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)
    # saving the Image
    cv2.imwrite('./sketches/sketch.png', sketch_img)
    return plt.imshow(sketch_img)
