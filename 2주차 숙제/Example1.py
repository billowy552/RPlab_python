import urllib.request
import gzip
import numpy as np
import os
from struct import *
import matplotlib
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

    train_img = open(os.path.splitext(file[0])[0], 'rb')
    train_lbl = open(os.path.splitext(file[1])[0], 'rb')
    test_img = open(os.path.splitext(file[2])[0], 'rb')
    test_lbl = open(os.path.splitext(file[3])[0], 'rb')

    img1 = np.zeros((28, 28))           # image를 위한 array 생성
    lbl1 = [[], [], [], [], [], [], [], [], [], []]             # 0~9의 레이블 생성
    img2 = np.zeros((28, 28))
    lbl2 = [[], [], [], [], [], [], [], [], [], []]

    s1 = train_img.read(16)             # 처음 16바이트 읽어냄
    l1 = train_lbl.read(8)              # 처음 8바이트 읽어냄
    s2 = test_img.read(16)
    l2 = test_lbl.read(8)

    i = 1
    while True:
        s1 = train_img.read(784)            # 28x28 byte씩 읽음
        l1 = train_lbl.read(1)
        s2 = test_img.read(784)
        l2 = test_lbl.read(1)

        if not s1 or not l1 or not s2 or not l2: break

        index1 = int(l1[0])         # 각 레이블에 해당하는 인덱스를 지정
        img1 = np.reshape(unpack(len(s1)*'B', s1), (28, 28))            # 28x28 배열로 디코딩(?)
        lbl1[index1].append(img1)           # 각 이미지의 숫자에 해당하는 레이블 저장
        if not os.path.exists("./train"):           # train 디렉토리 형성
            os.mkdir("./train")
        os.chdir('./train')             # train 디렉토리로 이동

        if not os.path.exists("./%d" % index1):         # 이미지의 숫자에 해당하는 폴더 생성 후 이동
            os.mkdir("./%d" % index1)
        os.chdir('./%d' % index1)

        matplotlib.image.imsave('%d.png' % i, img1)             # 숫자 폴더에 이미지 저장
        os.chdir('../../')              # 저장 후 mnist 디렉토리로 돌아감

        index2 = int(l2[0])             # 이후 test 폴더에 대해 똑같이 적용
        img2 = np.reshape(unpack(len(s2)*'B', s2), (28, 28))
        lbl2[index2].append(img2)
        if not os.path.exists("./test"):
            os.mkdir("./test")
        os.chdir("./test")

        if not os.path.exists("./%d" % index2):
            os.mkdir("./%d" % index2)
        os.chdir('./%d' % index2)

        matplotlib.image.imsave('%d.png' % i, img2)
        os.chdir('../../')

        i += 1


download_mnist('http://yann.lecun.com/exdb/mnist/')
