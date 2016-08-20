import pymysql

class Connection:
	def getConn():
		return pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='blogpost',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor);
 
		