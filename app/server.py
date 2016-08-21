from flask import Flask,render_template,request,redirect,url_for,make_response
from controllers.blogcontroller import BlogController

app = Flask(__name__)

#API Routes
# @Author Vincent Nacar

@app.route('/api/blogs')
def api_blogs():
	res = make_response(BlogController.render_json());
	res.mimetype = "application/json";
	return res;
	
@app.route('/api/blog/post',methods=['POST'])
def api_postblog():
	if request.method=='POST':
		userid = request.values['userid'];
		title = request.values['title'];
		body = request.values['body'];
		BlogController.post_blog(userid,title,body);
		return redirect(url_for('api_blogs'));

@app.route('/api/blog/delete/<int:id>',methods=['GET','POST'])
def api_deleteblog(id):
		BlogController.delete_blog(id);
		return redirect(url_for('api_blogs'));



if __name__ == '__main__':
	app.run(debug=True)