from flask import Flask,render_template,request
from controllers.blogcontroller import BlogController

app = Flask(__name__)

@app.route('/blog')
def blog_load():
	return BlogController.get_blogs();

@app.route('/blog/post',methods=['GET','POST'])
def blog_post():
	if request.method=='POST':
		return BlogController.post_blog();
	else:
		return "Invalid request";

@app.route('/blog/delete',methods=['GET','POST'])
def blog_delete():
	if request.method=='POST':
		return BlogController.delete_blog();
	else:
		return "Invalid request";
	
if __name__ == '__main__':
	app.run(debug=True)