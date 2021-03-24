#加载景点信息

def load_sp():
    s_file=open('北京数据\\北京景点名称.txt', 'r', encoding='utf-8', errors='ignore')
    a_file=open('北京数据\\北京景点地址.txt', 'r', encoding='utf-8', errors='ignore')
    c_file=open('北京数据\\北京景点评分.txt', 'r', encoding='utf-8', errors='ignore')
    name=[]
    adre=[]
    score=[]

    for line in s_file:
        line=line.strip()
        name.append(line)
    for line in a_file:
        line=line.strip()
        adre.append(line)
    for line in c_file:
        line=line.strip()
        line=line.rstrip(' 分')
        score.append(line)

    return name,adre,score              #景点名，景点地址，景点得分

