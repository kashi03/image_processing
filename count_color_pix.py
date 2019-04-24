from PIL import Image
import numpy as np
import glob

def color_count(img, index):
    np_img = np.asarray(img)
    return np.sum(np_img == index)

if __name__ == "__main__":
    imgs = glob.glob('.\\segment\\????-??-??-??-??-??.png')
    for i in imgs:
        img = Image.open(i)
        nums = []
        for index in range(9):
            nums.append(color_count(img, index))
        
        print(sum(nums))
        print(i, nums)
        break