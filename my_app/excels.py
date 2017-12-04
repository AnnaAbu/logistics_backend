import xlrd
import pymysql
import xlwt

#excel2db
def excel_dr(table_name):
    wb = xlrd.open_workbook('/×.xlsx')  # 打开excel文件
    sh = wb.sheet_by_index(0)  # sh 为excel中的sheet1
    dfun = []
    nrows = sh.nrows  # 行数
    ncols = sh.ncols  # 列数
    fo = []

    fo.append(sh.row_values(0))  # fo列表中添加sheet1中的第一行数据
    for i in range(1, nrows):
        dfun.append(sh.row_values(i))  # dfun列表添加sheet1中的第二行到最后一行数据

    conn = pymysql.connect(host='localhost', user='root', passwd='13313288898lzt', db='logistics')  # 连接数据库
    cursor = conn.cursor()  # 创建游标

    cursor.execute("create table "+table_name+"(" + fo[0][0] + " varchar(100));")  # 创建table命名test4，添加第一个字段名

    for i in range(1, ncols):
        cursor.execute("alter table "+table_name+" add " + fo[0][i] + " varchar(100);")  # 按列数，添加新字段名到table
    val = ''
    for i in range(0, ncols):  # 1到最后一列
        val = val + '%s,'  # %s指向字段名
    print(dfun)

    cursor.executemany("insert into resources_networkdevice values(" + val[:-1] + ");", dfun)  # 数据存入数据库
    conn.commit()
    cursor.close()
    conn.close()

#db2excel
def excel_dc(table_name):
    conn = pymysql.connect(host='localhost', user='root', passwd='13313288898lzt', db='logistics')
    cursor = conn.cursor()
    count = cursor.execute('select * from '+table_name)

    print('has %s record' % count)

    cursor.scroll(0, mode='absolute')  # 重置游标位置

    results = cursor.fetchall()  # 搜取所有结果 results=[[],[]]  len(results)个[],[]中有len(fields)个数
    # 测试代码，print results
    # 获取MYSQL里的数据字段
    fields = cursor.description  # 得到字段名称 field=[[],[],[]]

    wbk = xlwt.Workbook()  # 创建工作簿
    sheet = wbk.add_sheet(table_name, cell_overwrite_ok=True)  # 创建sheet
    for ifs in range(0, len(fields)):
        sheet.write(0, ifs, fields[ifs][0])  # 将字段写入到EXCEL新表的第一行
    ics = 1
    jcs = 0
    for ics in range(1, len(results) + 1):  # 从第二行开始写
        for jcs in range(0, len(fields)):
            sheet.write(ics, jcs, results[ics - 1][jcs])
    wbk.save('×××××/Desktop/'+table_name+'.xlsx')
