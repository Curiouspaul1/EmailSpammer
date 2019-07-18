
'''heroku link
https://pure-savannah-79098.herokuapp.com'''

#Dependencies
from flask import Flask,request,jsonify
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
#from config import uri
from flask_mail import Mail, Message
import random
import time

#instantiate flask app
app = Flask(__name__)

# Mail Server COnfig

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'paulcurious7@gmail.com',
    MAIL_PASSWORD = 'mechatronic',
))


mail = Mail(app)

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
@app.route('/')
def index():
	'''msg = Message('',sender='paulcurious7@gmail.com',recipients=['intheknoow@gmail.com'])
	text = 
			An electromagnetic pulse (EMP), also sometimes called a transient electromagnetic disturbance, is a short burst of electromagnetic energy. Such a pulse may occur in the form of a radiated electric or magnetic field or conducted electrical current depending on the source. EMP Jammer is a device capable of generating a transient electromagnetic disturbance that radiates outward from its epicenter, disrupting electronic devices
	for i in range(5):
		text = text.split()
		random.shuffle(text)
		text = ''.join(i + ' ' for i in text)
		msg.body = text
		mail.send(msg)
		time.sleep(60)'''
	for i in range(5):
		text = '''
			An electromagnetic pulse (EMP), also sometimes called a transient electromagnetic disturbance, is a short burst of electromagnetic energy. Such a pulse may occur in the form of a radiated electric or magnetic field or conducted electrical current depending on the source. EMP Jammer '''
		text = text.split()
		random.shuffle(text)
		text = ''.join(i + ' ' for i in text)
		msg = Message('',sender='paulcurious7@gmail.com',recipients=['intheknoow@gmail.com'])
		msg.body = text
		mail.send(msg)
		time.sleep(10)
	return 'Message sent'
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

