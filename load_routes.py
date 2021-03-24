#加载收集了旅游路线信息

def load_route(path):
    #打开待处理文件
    file=open(path, 'r', encoding='utf-8', errors='ignore')         ##############
    route=[]
    for line in file:
        r=[]
        r=line.split()
        route.append(r)
    file.close()

    return route                          #景点序列


#根据景点名和路线建立景点先后矩阵

def spot_mat(spots,routes):
    spot_dic={}                      #景点名和位置的映射
    n=0
    for s in spots:
        spot_dic[s]=n
        n=n+1
    
    order_mat=[]                       #景点先后矩阵   order_mat[i][j] 表示i景点之后去j景点有多少次
    for i in range(n):
        order_mat.append([])
        for j in range(n):
            order_mat[i].append(0)
    
    for r in routes:
        for i in range( len(r)-1 ):
            if(r[i] in spot_dic and r[i+1] in spot_dic ):
                order_mat[ spot_dic[r[i]] ][spot_dic[r[i+1]]]+=1
    
    return spot_dic,order_mat
    
    




