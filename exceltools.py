import xlrd

# 读取excel的方法
def read_excel(excel_path, sheet_name, skip_first=True):
    """
        方法：读取excel
        参数：
            excel_path：excel的文件路径
            sheet_name：要读取的excel的sheet名字
            skip_first：是否跳过首页，默认跳转，True跳过，False：不跳过
        返回值：[[row1], [row2], [row3],....]
    """
    results = []
    datas = xlrd.open_workbook(excel_path)
    table = datas.sheet_by_name(sheet_name)
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行的数据
    for row in range(start_row, table.nrows): # (1,4)
        results.append(table.row_values(row))

    return results

# path = "data\\测谈网接口测试用例.xlsx"
# sn = 'Sheet1'
# res = read_excel(path, sn)
# print(res)