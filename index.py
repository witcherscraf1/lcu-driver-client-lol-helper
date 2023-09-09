import xlrd

'''
input:
      excel文件名，表单序号
output:
      result:将excel表格内容变为由字典组成的list变量，便于之后的查找
      ref:是字典，为查找对应英雄的result值查找提供参考关系，如result[dict['夏洛特']]
'''
def get_data(filename, sheetnum):
    dir_case = filename
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[sheetnum]
    ##得到该excel表格的有效行数和列数
    nor = table.nrows
    nol = table.ncols
    result = []
    ref = {}
    for i in range(1,nor):
        data_row = {}
        ##将每一行（每一个英雄）的数据制作相应的字典data_row后加入到result中
        for j in range(nol):
            title = table.cell_value(0,j)
            value = table.cell_value(i,j)
            data_row[title] = value
        result.append(data_row)
        ref[table.cell_value(i,0)] = i - 1      #以英雄名作为key，对应的value是i-1，便于之后查找
        

    return result,ref