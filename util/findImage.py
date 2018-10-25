# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 16:48
# @Author  : 留仙洞
# @FileName: findImage.py
# @Software: PyCharm
import os
# import cv2
from glob import glob
import hashlib
import logging
from PIL import Image
img_size = 0
totalImageSize = 0
totalOtherSize = 0
CUR_FULL_PATH = os.getcwd()
#输出路径
OUTPUT_PATH = os.path.join(CUR_FULL_PATH, "pic_same.csv")
#图片路径
PIC_SIZE_PATH = os.path.join(CUR_FULL_PATH, "pic_over_size.csv")
def find_dir(dir_path):
    # root:根路径；dirs:文件路径；files：文件
    full_paths =[]
    for root ,dirs ,files in os.walk(dir_path):
        for file in files:
            # 全路径
            full_path = os.path.join(root,file)
            if full_path.endswith(".png"):
                # 获取所有的图片
                full_paths.append(full_path)
                # print("file：%s"+full_path)
                # return full_paths
    print(full_paths)
    return full_paths


def checkSameResource(dir_path,f):
    # 获取md5的资源
    md5Dict = get_all_md5(dir_path)
    for root , dirs , files in os.walk(dir_path):
        for file in files:
            fileFullPath = os.path.join(root,file)
            # print(fileFullPath)
            md5 = get_md5(fileFullPath)
            same_files = md5Dict[md5]
            # print(len(same_files))
            if len(same_files) >= 1:
                if fileFullPath.endswith(".png") or fileFullPath.endswith(".jpg") or fileFullPath.endswith("..JPG"):
                    # 写进图片信息中去
                    writeImageInfo(f,fileFullPath,same_files)

def writeImageInfo(f,file_full_path,files):
    global totalImageSize
    img = Image.open(file_full_path)
    totalImageSize = os.path.getsize(file_full_path)
    f.write(file_full_path + ',')
    f.write(img.format + ',')
    f.write(str(img.size[0]) + ',')
    f.write(str(img.size[1]) + ',')
    f.write(str(os.path.getsize(file_full_path)/1024) + ',')
    f.write(str(len(files))+ ',')
    for file in files:
        f.write(str(file) + ',')
    f.write('\n')



def get_md5(file_full_path):
    '''
    获取md5码
    :param dir_path:
    :return:
    '''
    if not os.path.isfile(file_full_path):
        return
    myhash = hashlib.md5()
    f = open(file_full_path,'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
def get_all_md5(dir_path):
    md5Drict = {}
    for root ,dirs, files in os.walk(dir_path):
        for file in files:
            filelist = []
            file_full_path = os.path.join(root,file)
            md5 = get_md5(file_full_path)
            if md5 not in md5Drict.keys():
                filelist.append(file_full_path[len(dir_path)+1:])
                md5Drict[md5] = filelist
            else:
                md5Drict[md5].append(file_full_path[len(dir_path)+1:])
    print("md5Drict"+str(md5Drict))
    return md5Drict

if __name__ == "__main__":
    # get_all_image("C:\\Users\\admin\\Pictures")
    dir_path = 'C:\\Users\\admin\Pictures'
    if os.path.exists(OUTPUT_PATH):
        os.remove(OUTPUT_PATH)
    f = open(OUTPUT_PATH,"w")
    f.write("path,format,width,height,size,count,file1,file2,file3,file4,file5\n")
    # for file in dir_path:
    checkSameResource(dir_path,f)
    print("totalImageSize:"+ str(totalImageSize))
    f.write('totalImageSize' + ',' + str(totalImageSize/1024) + 'K\n')
    f.close()
    # for file in dir_path:

