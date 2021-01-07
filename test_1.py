import cv2
import numpy as np
import os


def resize_img(img):
    height, width = img.shape[0], img.shape[1]
    td_num = img.shape[2]
    if height < width:
        zero = np.zeros((width, width, td_num), dtype=np.uint8)
        start_num = int((width - height) / 2)
        zero[start_num:start_num + height] = img[:]
        return zero
    elif height > width:
        zero = np.zeros((height, height, td_num), dtype=np.uint8)
        start_num = int((height - width) / 2)
        for i in range(height):
            zero[i][start_num:start_num + width] = img[i]
        return zero
    else:
        return img


if __name__ == '__main__':
    ori_img_path = '.\\data\\ori_images\\'
    re_img_path = '.\\data\\re_images\\'
    re_416_path = '.\\data\\re_416_images\\'

    img_paths = os.listdir(ori_img_path)
    for i in img_paths:
        img_path = os.path.join(ori_img_path, i)
        img = cv2.imread(img_path)
        re_img = resize_img(img)
        re_name = 're_' + i
        save_path = os.path.join(re_img_path, re_name)
        cv2.imwrite(save_path, re_img)

    print('共处理了%s张图片' % (len(img_paths)))

    # 改变图像大小
    re_img_paths=os.listdir(re_img_path)
    for i416 in re_img_paths:
        img = os.path.join(re_img_path, i416)
        im1 = cv2.imread(img)
        im2 = cv2.resize(im1, (416, 416), )  # 为图片重新指定尺寸
        re_416_name = '416_'+i416
        save_416_path=os.path.join(re_416_path, re_416_name)
        cv2.imwrite(save_416_path, im2)
    print('416共处理了%s张图片' % (len(re_img_paths)))