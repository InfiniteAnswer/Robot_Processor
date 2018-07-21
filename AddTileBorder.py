import os
import cv2


path = 'c:/users/v_sam/documents/PxlRT/TileImages/tiles_new/'
borderWidth = 1.5/23

print(os.listdir(path))
for filename in os.listdir(path):
    img = cv2.imread(path+filename)
    tile_length = img.shape[0]
    border_pixels = int(tile_length*borderWidth)
    new_img = cv2.copyMakeBorder(img, border_pixels, border_pixels, border_pixels, border_pixels,
                                 cv2.BORDER_CONSTANT, None, [255,255,255])
    cv2.imwrite(path+filename, new_img)