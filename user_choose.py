import numpy


import numpy as np


def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a
    :param vector_b: 向量 b
    :return: sim
    """
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


def user_vec(mat,name_dic,spot_names):
    v=numpy.zeros(len(mat[0]))
    for name in spot_names:
        i=name_dic[name]
        v+=mat[i]
    v=v/[len(spot_names)]
    return v

def user_spot(mat,user_v,n):
    i_sim= {}
    for i in range(len(mat)):
        s=cos_sim(mat[i],user_v)
        i_sim[i]=s

    si_sim=dict(sorted(i_sim.items(), key=lambda item: item[1], reverse=True))
    spos=[]
    for key,value in si_sim.items():
        spos.append(key)
        if(len(spos)==n):
            break
    return spos