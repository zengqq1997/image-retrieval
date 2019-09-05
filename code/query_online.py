# -*- coding: utf-8 -*-
from extract_cnn_vgg16_keras import VGGNet

import numpy as np
import h5py
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse


def url_is_correct(index_t):
    if index_t > 5:
        print('超出请求次数！！！')
        exit()

    try:
        # url = input('请输入正确的图片路径：')

        queryDir = path

        src = mpimg.imread(queryDir)
        return queryDir

    except:
        print('有误的图片路径，请重新输入：')
    return url_is_correct(index_t + 1)


def query_online(path):
    ap = argparse.ArgumentParser(description="This is a example program ")
    # ap.add_argument("-query", required = False, default='TestImages/0.png',
    #	help = "Path to query which contains image to be queried")
    # ap.add_argument("-index", required = False,default='LACEfeatureCNN.h5',
    # 	help = "Path to index")
    # ap.add_argument("-result", required = False,default='lace',
    # 	help = "Path for output retrieved images")
    # 总数据
    ap.add_argument("-index", required=False, default='model1.h5',
                    help="Path to index")
    ap.add_argument("-result", required=False, default='img',
                    help="Path for output retrieved images")

    args = vars(ap.parse_args())

    # 读入索引图像的特征向量和相应的图像名称
    h5f = h5py.File(args["index"], 'r')
    # feats = h5f['dataset_1'][:]
    feats = h5f['dataset_1'][:]
    print("111", feats)
    imgNames = h5f['dataset_2'][:]
    print("222", imgNames)
    h5f.close()

    # print("--------------------------------------------------")
    # print("               searching starts")
    # print("--------------------------------------------------")
    # print('----------**********-------------')
    # op = input("退出请输 exit，查询请输 enter : ")
    # if op == 'exit':
    #     break
    # else:
    # read and show query image
    # 设置多张图片共同显示
    # figure, ax = plt.subplots(4, 4)
    global index_t
    index_t = 1

    # init VGGNet16 model
    model = VGGNet()

    # 提取查询图像的功能，计算simlarity得分和排序
    queryVec = model.extract_feat(path)
    # print (queryVec)
    name=str(path).split('/')[10]
    print (name)
    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]
    #print(rank_score)

    # number of top retrieved images to show
    maxres = 15
    imlist=[]
    all_scores =[]
    for i in  range(0,imgNames.shape[0]):

        if (imgNames[i].split(b'_')[0]==imgNames[rank_ID[0]].split(b'_')[0]):
            all_scores.append(scores[i])
            imlist.append(imgNames[i])
    rank_index=np.argsort(all_scores)[::-1]
    all_scores.sort(reverse=True)
    # print(all_scores)
    # print (rank_index)
    # print (imlist)
    # print (imgNames[rank_ID[0]])
    sum=0
    imlist1 = [imlist[index] for i, index in enumerate(rank_index[0:maxres])]
    # print (imlist1)
    # for i in range(0,maxres):
    #     if(imlist1[i].split(b'_')[0]==imgNames[rank_ID[0]].split(b'_')[0]):
    #         sum=sum+1
    # print (sum)
    print("top %d images in order are: " % maxres, imlist1)

    # # show top #maxres retrieved result one by one
    # for i,im in enumerate(imlist):
    #     image = mpimg.imread(args["result"]+"/"+str(im, 'utf-8'))
    #     plt.title("search output %d" %(i+1))
    #     plt.imshow(image)
    #     plt.show()

    # 显示多张图片

    # for i, im in enumerate(imlist):
    #     image = mpimg.imread(args["result"] + "/" + str(im, 'utf-8'))
    #     im_name = str(im).split('\'')[1]
    #     ax[int((i + 1) / 4)][(i + 1) % 4].set_title('%d Image %s -- %.2f' % (i + 1, im_name, rank_score[i]),
    #                                                 fontsize=10)
    #     # ax[int(i/maxres)][i%maxres].set_title('Image_name is %s' % im,fontsize=2)
    #     ax[int((i + 1) / 4)][(i + 1) % 4].imshow(image, cmap=plt.cm.gray)
    #     ax[int((i + 1) / 4)][(i + 1) % 4].axis('off')
    # plt.show()
    return imlist1,args,all_scores
