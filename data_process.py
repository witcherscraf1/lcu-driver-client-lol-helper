'''
function:对数据进行归一化，便于之后对数据做出综合评价
input:
      输入原始数据，即index的返回值result
output:
      wholeChart中数据完成归一化后的list
'''

def process_data(wholeChart):  # 输入原始表格，输出数据归一化的表格。
    #胜率一栏进行归一化
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['胜率'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['胜率']=round(temp[i]/max_temp,3)

    #登场率
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['登场率'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['登场率']=round(temp[i]/max_temp,3)

    #ban率
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['ban率'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['ban率']=round(temp[i]/max_temp,3)

    #克制指数1
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['克制指数1'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['克制指数1']=round(temp[i]/max_temp,3)

    #克制指数2
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['克制指数2'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['克制指数2']=round(temp[i]/max_temp,3)

    #克制指数3
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['克制指数3'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['克制指数3']=round(temp[i]/max_temp,3)

    #被克制指数1
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数1'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数1']=round(temp[i]/max_temp,3)

    #被克制指数2
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数2'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数2']=round(temp[i]/max_temp,3)

    #被克制指数3
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数3'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数3']=round(temp[i]/max_temp,3)

    #被克制指数2
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数2'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数2']=round(temp[i]/max_temp,3)

    return wholeChart

#####################
#函数功能：由名称获得该英雄的数据
#eg: get_data_from_name(wholeChart,'夏洛特')
def get_data_from_name(wholeChart,name):
    for i in range(len(wholeChart)):
        if name == wholeChart[i]['英雄名称']:
           # print("成功获取")
            return wholeChart[i]
   
    return 'error,please check it again'





    