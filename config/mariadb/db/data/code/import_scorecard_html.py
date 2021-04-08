import os
import pymysql as pysql

#連線資料庫
connection = pysql.connect(
  host='localhost', 
  port=3306, 
  user='root',
  password='qaz123456789',
  db='analysis',
  charset='utf8', 
  cursorclass = pysql.cursors.DictCursor
  )
#把sql語句運送到database執行的載具
cursor = connection.cursor()
a = 0
category_r, file_r = [], []
def extractlist(command):
  result = os.popen(command)
  result = str(result.read())
  result = result.split("\n")
  del(result[-1])
  return result
category_r = extractlist("ls ../scorecard/ct_value_/")
for ele in category_r:
  file_r = extractlist("ls ../scorecard/ct_value_/" + ele + "/interpolate/")
  for i in file_r:
    j = i.strip('.html')
    sql = "INSERT INTO `Scorecard_CT_values` VALUE (\'" + j + "\',\'" + ele + "\',\'scorecard/ct_value_/"+ ele +"/interpolate/" + i + "\');" 
    a += 1
    try:
      cursor.execute(sql)
      connection.commit()
    except Exception as e:
      connection.rollback()
      print(str(e))

  #檢查用
  #print(a)  
connection.close()
