from flask import Flask,render_template
from models.blogs import blogs

class BlogController:
	def render():
		data = blogs.all_blogs();
		return render_template('post.tpl.html',blogsdata = data)
	def post_blog(userid,title,body):
		blogs.blog_insert(userid,title,body);
		return;
		
	def delete_blog(id):
		blogs.blog_delete(id);
		return;
		
	def get_blogs():
		return blogs.all_blogs();
