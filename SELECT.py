#-*-coding:gb2312-*-
import json

import pymysql
# import re
liveroomurl = open('liveroomurl.txt','a')#---------存放roomurl
livelogurl = open('livelogurl.txt','a')#-----------存放livelogurl
category_idFile = open('0010.txt')#----------------存放category_id的文件

pageSize = 1000

#数据库连接
db = pymysql.connect(host='10.234.128.66',user='',password='',port=3332,db='live',charset='utf8')



#筛选出url的方法
def urlscreen(data):
    if data!=None and data!='':
        data_dict = json.loads(data)
        for key in data_dict:
            if key == 'banner':
                banner_value = data_dict.get('banner')
                urlkey = ['url','liveUrl','newsUrl','topUrl']
                for url_key in urlkey:
                    if banner_value.get(url_key)!=''and banner_value.get(url_key):
                        liveroomurl.write(banner_value.get(url_key)+'\n')
                        print(banner_value.get(url_key))

for category_id in category_idFile.readlines():
    category_id = category_id.strip()
    #----------------------------------首先处理第一张表----------------------------------------------------------------
    offset = 0
    while True:
        sql1 = "SELECT  `ID`,  `NAME`, `APP_CONFIG`,  `PC_CONFIG`, `SHARE_IMAGE` FROM `live`.`room` WHERE category_id=" \
               +str(category_id)+" and end_date < '2022-1-1' "+" ORDER BY `ID` limit "+str(pageSize)+" offset "+str(offset)
        print("category_id=",category_id,"查询第",offset,"--",pageSize+offset,"条")

        offset += pageSize

        #执行sql语句，返回result为（（），（），（），...........）
        cursor = db.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()

        for r in result:
            print("category_id="+str(category_id)+"的，ID="+str(r[0]))
            try:

                urlscreen(r[2])
                urlscreen((r[3]))
                if r[4]!=None and r[4]!='':
                    liveroomurl.write(r[4]+'\n')
            except:
                continue


            #-----------------------------------开始处理第二张表-----------------------------
            offset2 = 0
            while True:
                sql2 = "SELECT `id`, `room_id`, `message` FROM `live`.`live_log` WHERE room_id="+str(r[0])+" limit "+str(pageSize)+" offset "+str(offset2)
                print("offset=",offset2)
                offset2 += pageSize

                cursor = db.cursor()
                cursor.execute(sql2)
                result2 = cursor.fetchall()

                for r2 in result2:
                    print("room_id=", r2[1])
                    data_dict = json.loads(r2[2])
                    try:
                        url = data_dict.get('imgSrc')
                        if'@'in url:
                            url = url.replace('@',"\n")
                        print(url)
                        livelogurl.write(url+'\n')
                    except:
                        continue
                # 判断 查出来的result小于pageSize,最后一页跳出循环
                if len(result2)<pageSize:
                    break


        #判断 查出来的result小于pageSize,最后一页跳出循环
        if len(result)<pageSize:
            break




