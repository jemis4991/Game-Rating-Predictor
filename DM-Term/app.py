import os
import shutil
import csv
import sys
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
import joblib
import numpy as np

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'

class NameForm(FlaskForm):
	name = StringField('Comment', default="Worst Game")
	submit = SubmitField('Submit')

# ROUTES!
@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		x = form.name.data
		sam=[x]
		vector = joblib.load('vectorizer.sav')
		mnb = joblib.load('mnb.sav')
		text = vector.transform(sam)
		result = mnb.predict(text)
		result=str(result).strip('[.]')
		return render_template('index.html',form=form,result=result)
	return render_template('index.html',form=form,result=None)

@app.route('/help')
def help():
	text_list = []
	# Python Version
	text_list.append({
		'label':'Python Version',
		'value':str(sys.version)})
	# os.path.abspath(os.path.dirname(__file__))
	text_list.append({
		'label':'os.path.abspath(os.path.dirname(__file__))',
		'value':str(os.path.abspath(os.path.dirname(__file__)))
		})
	# OS Current Working Directory
	text_list.append({
		'label':'OS CWD',
		'value':str(os.getcwd())})
	# OS CWD Contents
	label = 'OS CWD Contents'
	value = ''
	text_list.append({
		'label':label,
		'value':value})
	return render_template('help.html',text_list=text_list,title='help')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')

port = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port)