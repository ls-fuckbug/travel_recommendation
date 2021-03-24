import lda
from lda import *
import data_process
from data_process import all_words
import tfidf
from tfidf import tfidf_vc
import load_spot
from load_spot import load_sp
import user_choose
from user_choose import *


print("This is project belong to sam")

# all_wd=all_words('北京数据\\北京景点评论总.txt')
#
# wdic,weight_mat=tfidf_vc(all_wd)
# #训练lda模型
# lda_model(weight_mat)


#加载lda模型
docres = load_lda_doc()
print(len(docres))  # 文档数目
print(len(docres[0]))  # 主题数目

name,adre,score=load_sp()

name_dic={k: v for v, k in enumerate(name)}

print(name_dic)

spot_name=['北海公园','居庸关长城','中山公园','法源寺']
v=user_vec(docres,name_dic,spot_name)
print(len(v))
print(v)

spos=user_spot(docres,v,10)
print(spos)
for i in spos:
    print(name[i])