from flask import Flask,render_template,request,redirect,url_for
from controllers.blogcontroller import BlogController

app = Flask(__name__)

@app.route('/blog')
def blog_load():
	return BlogController.render();

@app.route('/blog/post',methods=['GET','POST'])
def blog_post():
	if request.method=='POST':
		userid = request.form['userid'];
		title = request.form['txttitle'];
		body = request.form['txtbody'];
		BlogController.post_blog(userid,title,body);
		return  redirect(url_for('blog_load'))
	else:
		return BlogController.render();

@app.route('/blog/delete/<int:id>',methods=['GET','POST'])
def blog_delete(id):
	BlogController.delete_blog(id);
	return  redirect(url_for('blog_load'))
	
if __name__ == '__main__':
	app.run(debug=True)