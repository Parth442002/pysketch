import cv2
from django.forms import NullBooleanField
import matplotlib.pyplot as plt
from zmq import NULL


def img2sketch(photo, hd=NULL):
    if hd == NULL:
        k_size = 111
    elif hd == 'High Definition':
        k_size = 333
    elif hd == 'Standard Definition':
        k_size = 55
    # Read Image
    img = cv2.imread(photo)

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)
    # invert_img=255-grey_img

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (k_size, k_size), 0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(blur_img)
    # invblur_img=255-blur_img

    # Sketch Image
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)

    # Save Sketch
    #cv2.imwrite('sketch.png', sketch_img)
    rgb_sketch_img = cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)

    # Display sketch
    plt.imshow(rgb_sketch_img)
