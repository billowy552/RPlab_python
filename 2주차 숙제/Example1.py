import urllib.request
import gzip
import numpy as np
import os
from struct import *
import matplotlib.image
import matplotlib.pyplot as plt
from PIL import Image


def download_mnist(url):

    file = ["train-images-idx3-ubyte.gz",
            "train-labels-idx1-ubyte.gz",
            "t10k-images-idx3-ubyte.gz",
            "t10k-labels-idx1-ubyte.gz"]            # url의 file link

    if not os.path.exists("./mnist"):
        os.mkdir("./mnist")         # mnist 디렉토리 생성

    os.chdir("./mnist")
    print("현재 디렉토리 : ", os.getcwd())
    contents = []
    for i in range(4):
        file_url = url + file[i]            # full link
        urllib.request.urlretrieve(file_url, file[i])           # link에서부터 파일 다운로드
        raw_file = os.path.splitext(file[i])[0]
        with gzip.open(file[i], "rb") as f:
            contents.append(f.read())
            with open(raw_file, 'wb') as w:
                w.write(contents[i])            # 압축해제하여 파일 저장

    train_img = os.path.splitext(file[0])[0]
    train_lbl = os.path.splitext(file[1])[0]
    test_img = os.path.splitext(file[2])[0]
    test_lbl = os.path.splitext(file[3])[0]

    train_dir = './train'
    test_dir = './test'
    if not os.path.exists(train_dir): os.mkdir(train_dir)
    if not os.path.exists(test_dir): os.mkdir(test_dir)

    def save_img(byte_img_file, byte_lbl_file, save_dir):
        img_file = open(byte_img_file, 'rb')
        lbl_file = open(byte_lbl_file, 'rb')

        s = img_file.read(16)
        l = lbl_file.read(8)

        while True:
            s = img_file.read(784)            # 28x28 byte씩 읽음
            l = lbl_file.read(1)

            if not s or not l: break

            index = int(l[0])         # 각 레이블에 해당하는 인덱스를 지정
            img = np.reshape(unpack(len(s)*'B', s), (28, 28))            # 28x28 배열로 디코딩(?)

            save_folder = os.path.join(save_dir, str(index))
            if not os.path.exists(save_folder): os.mkdir(save_folder)        # /train/(숫자레이블) 디렉토리 형성
            os.chdir(save_folder)

            matplotlib.image.imsave(str(len(os.listdir('./'))+1)+'.png', img)     # 숫자 폴더에 이미지 저장
            os.chdir('../../')

        return None

    save_img(train_img, train_lbl, train_dir)
    save_img(test_img, test_lbl, test_dir)


download_mnist('http://yann.lecun.com/exdb/mnist/')
