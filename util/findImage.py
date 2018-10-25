# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 16:48
# @Author  : 留仙洞
# @FileName: findImage.py
# @Software: PyCharm
import os
# import cv2
from glob import glob
import hashlib
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
            md5 = get_md5(fileFullPath)
            same_files = md5Dict[md5]
            if len(same_files) > 1:
                if fileFullPath.endswith(".png") or fileFullPath.endswith(".jpg"):
                    # 写进图片信息中去
                    writeImageInfo(f,fileFullPath[len(dir_path)+1:],same_files)


def writeImageInfo(f,image_full_path,files):
    img = Image.open(image_full_path)
    totalImageSize = os.path.getsize(image_full_path)
    f.write(image_full_path + ',')
    f.write(img.format + ',')
    f.write(str(img.size[0]) + ',')
    f.write(str(img.size[1]) + ',')
    f.write(str(os.path.getsize(image_full_path)/1024) + ',')
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
    return md5Drict
#
# def get_all_image(dir_path):
#     '''
#     获取图片和大小
#     :param filename:
#     :return:
#     '''
#     # find_dir(dir_path)
#     img_list = []
#     global img_size
#     for img_path in find_dir(dir_path):
#         img = os.path.splitext(img_path)
#         im = Image.open(img_path)
#         im_size =im.size
#         img_size = os.path.getsize(img_path)
#         img_list.append(im)
#         # for img_cp in img_list:
#         #     img_cp
#         # print("图片名称："+img_path+"图片尺寸:"+str(im_size)+"--图片大小:"+str(img_size/1024))
#     print("图片:%s"+str(img_list))



if __name__ == "__main__":
    # get_all_image("C:\\Users\wb.liuxiandong\Documents\GitHub\Casino_Client\Assets")
    dir_path = 'C:\\Users\wb.liuxiandong\Documents\GitHub\Casino_Client\Assets'
    if os.path.exists(OUTPUT_PATH):
        os.remove(OUTPUT_PATH)
    f = open(OUTPUT_PATH,"w+")
    f.write("path,format,width,height,size,count,file1,file2,file3,file4,file5\n")
    for file in dir_path:
        checkSameResource(file,f)
    print(totalImageSize)
    f.write('totalImageSize' + ',' + str(totalImageSize/1024) + 'K\n')
    f.close()
    # for file in dir_path:

