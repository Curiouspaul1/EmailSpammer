#Dependencies
from flask import Flask,request,jsonify
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
#from config import uri
from smtplib import SMTP

# instantiate smtpObject
smptpObj = SMTP()

#instantiate flask app
app = Flask(__name__)

#configurations
#app.config['SQLALCHEMY_DATABASE_URI'] = uri
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# instantiate db and marshmallow
#db = SQLAlchemy(app)
#ma = Marshmallow(app)

# Models 
'''class user_data(db.Model):
	id = db.Column(db.Integer,primary_key=True,nullable=False)
	email = db.Column(db.String(100),unique=True)
	frequency = db.Column(db.Integer)

	def __init__(self,email,frequency):
		self.email = email
		self.frequency = frequency

#Create Schema
class user_dataSchema(ma.Schema):
	class Meta:
		fields = ("email","frequency")

# Init Schema
userSchema = user_dataSchema(strict=True)  # single user object schema
users_Schema = user_dataSchema(many=True,strict=True) # multiple user object schena
'''
@app.route('/rec',methods=['GET','POST'])
def rec():
	#Get Data
	email = request.json['email']
	frequency = request.json['frequency']

	#create user_data
	'''newData = user_data(email,frequency)

	#Add to db
	db.session.add(newData)
	db.session.commit()

	return userSchema.jsonify(newData)'''

if __name__ == '__main__':
	app.run(debug=True)