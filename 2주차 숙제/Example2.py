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
        for index in sorted(os.listdir(os.path.join(root, phase))):         # index는 train 또는 test폴더 안의 숫자 label 폴더
            for f in sorted(os.listdir(os.path.join(root, phase, index))):          # f는 해당 숫자 폴더에 있는 파일
                self.img_list.append(os.path.join(root, phase, index, f))           # img_list 에 파일을 추가

        # 각 숫자의 image 개수에 따라 list_img 의 인덱스가 갖는 해당 숫자를 딕셔너리로 부여
        temp_list = [len(os.listdir(os.path.join(root, phase, '0')))]
        self.idx_dic = {0: list(range(temp_list[0]))}
        for i in range(1, 10):
            temp_list.append(temp_list[i-1] + len(os.listdir(os.path.join(root, phase, '%d' % i))))
            self.idx_dic[i] = list(range(temp_list[i-1], temp_list[i]))

    def __getitem__(self, index):
        idx = random.choice(self.idx_dic[index])            # 인덱싱한 숫자에 해당하는 딕셔너리의 이미지 리스트에서 랜덤으로 파일 불러오기
        img = cv2.imread(self.img_list[idx])
        lbl = int(self.img_list[idx].split('\\')[-2])           # 파일 경로의 끝에서 두번째가 인덱싱한 숫자 폴더에 해당

        return img, lbl


dataset = Dataset(root='mnist', phase='train')
image, label = dataset[7]
plt.imshow(image, cmap='gray')
plt.show()
print('Number :', label)
