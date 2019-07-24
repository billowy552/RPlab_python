# Example2.py
import os
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import cv2
import random


class Dataset:
    def __init__(self, root, phase):
        self.root = root
        self.phase = phase
        self.img_list = []
        for index in sorted(os.listdir(os.path.join(root, phase))):
            for f in sorted(os.listdir(os.path.join(root, phase, index))):
                self.img_list.append(os.path.join(root, phase, index, f))

        temp_list = [len(os.listdir(os.path.join(root, phase, '0')))]
        self.idx_dic = {0: list(range(temp_list[0]))}
        for i in range(1, 10):
            temp_list.append(temp_list[i-1] + len(os.listdir(os.path.join(root, phase, '%d' % i))))
            self.idx_dic[i] = list(range(temp_list[i-1], temp_list[i]))

    def __getitem__(self, index):
        idx = random.choice(self.idx_dic[index])
        img = cv2.imread(self.img_list[idx])
        lbl = int(self.img_list[idx].split('\\')[-2])

        return img, lbl


dataset = Dataset(root='mnist', phase='train')
image, label = dataset[7]
plt.imshow(image, cmap='gray')
plt.show()
print('Number :', label)
