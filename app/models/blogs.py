from models.connection import Connection

class blogs:
	def all_blogs():
		cur = Connection.getConn().cursor();
		cur.execute('select * from blogs');
		return str(cur.fetchall());
	def blog_insert(userid,title,body):
		param = (userid,title,body);
		cur = Connection.getConn().cursor();
		cur.execute("INSERT INTO `blogs` (`blogid`, `userid`, `title`, `body`, `created`) VALUES (%s,%s,%s)",param);
		cur.commit();
		return;