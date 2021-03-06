"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request,make_response
from BlogApiPy import app
from BlogMySqlDataService import BlogMySqlDataService 
dataService=BlogMySqlDataService("root","xavi@1234")
dataService.createDatabase()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api/blogpost', methods = ['GET'])
def getAll():
    allPost= dataService.getAllPost()
    return make_response(jsonify(allPost))

@app.route('/api/blogpost', methods = ['POST'])
def SavePost():
    data = request.get_json()
    dataService.savePost(data["title"],data["discription"],data["author"],data["publishDate"],data["picture"])
    return make_response(jsonify('blog post created',"200"))

