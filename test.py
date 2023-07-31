#()()())()()
import row as row

import xlwt


def writeinexcel():
    f = open('a.txt', 'r', encoding='utf-8')  # 打开数据文本文档，注意编码格式的影响
    wb = xlwt.Workbook(encoding='utf-8')  # 新建一个excel文件
    ws1 = wb.add_sheet('first')  # 添加一个新表，名字为first
    # ws1.write(0, 0, 'mate1')
    # ws1.write(0, 1, 'h1')
    # ws1.write(0, 2, 'is_gum1 ')
    # ws1.write(0, 3, ' mate2')
    # ws1.write(0, 4, 'h2')
    # ws1.write(0, 5, 'is_gum2')
    # ws1.write(0, 6, 'mate3')
    # ws1.write(0, 7, 'h3')
    # ws1.write(0, 8, 'is_gum3')
    # ws1.write(0, 9, 'iactual2')
    # ws1.write(0, 10, 'ref_fqf_actual_value')
    # ws1.write(0, 11, 'weldtimeactualvalue')
    row = 0  # 写入的起始行
    col = 0  # 写入的起始列
    #通过row和col的变化实现指向单元格位置的变化
    k =1
    for lines in f:
        a = lines.split('\n') #txt文件中每行的内容按逗号分割并存入数组中
        k+=1
        for i in range(len(a)):
            ws1.write(row, col ,a[i])#向Excel文件中写入每一项
            col += 1
        row += 1
        col = 0

    wb.save("数据表.xls")
if __name__ == "__main__":
    writeinexcel()
