from models.connection import Connection

class blogs:
	def all_blogs():
		cur = Connection.getConn().cursor();
		cur.execute('select * from blogs');
		return cur.fetchall();
	def blog_insert(userid,title,body):
		conn = Connection.getConn();
		param = (userid,title,body);
		cur = conn.cursor();
		cur.execute("INSERT INTO `blogs` ( `userid`, `title`, `body`, `created`) VALUES(%s,%s,%s,CURRENT_TIMESTAMP)",param);
		conn.commit();
		return;
	def blog_delete(id):
		conn = Connection.getConn();
		param = (id);
		cur = conn.cursor();
		cur.execute("DELETE FROM `blogs` WHERE blogid = %s",param);
		conn.commit();
		return;		