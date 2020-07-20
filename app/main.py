from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)
ma =Marshmallow(app)

class  Questions(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	qcategory=db.Column(db.String(10))
	question=db.Column(db.Text)
	correct_option=db.Column(db.String(10))

	def __init__(self,qcategory,question,correct_option):
		self.qcategory=qcategory
		self.question=question
		self.correct_option=correct_option


class  Options(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	qid=db.Column(db.Integer)
	options=db.Column(db.Text)
	option_code=db.Column(db.String(10))

@app.route('/question/<string:category>/<int:qid>',methods=['GET'])
def questions(category,qid):
	y=0
	op_dict={}
	question=Questions.query.filter_by(qcategory=category)
	for x in question:
		y=y+1
		if y==qid:
			option=Options.query.filter_by(qid=x.id)
			for op in option:
				op_dict.update({op.option_code:op.options})
			new_dict=[{'question':x.question,
					'options':[op_dict]}]
	
	qstn=jsonify(new_dict)
	return qstn