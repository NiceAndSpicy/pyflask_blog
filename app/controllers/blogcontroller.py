from flask import Flask,render_template
from models.blogs import blogs

class BlogController:
	def render():
		return render_template('blog.tpl.html')
	def post_blog():
		return "blog posted";
		
	def delete_blog():
		return "blog deleted";
		
	def get_blogs():
		return blogs.all_blogs();
