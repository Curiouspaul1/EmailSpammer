
#A deployed version to play around with (link below)
'''heroku link
https://pure-savannah-79098.herokuapp.com'''

'''
	Just wanted to explain that the commented out code
	aren't just for show i used them to test out a restful
	version of this app that sends json data - made use of
	postman to send json if you look through the commented
	lines you probaably see that already - so if you like
	salvage what you can '''

#Dependencies
from flask import Flask,request,jsonify,render_template
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
	return render_template('index.html')

@app.route('/sendmail',methods=['GET','POST'])
def sendmail():
	#Get Data
	email = request.form['email']
	frequency = request.form['frequency']
	frequency = abs(eval(frequency))

	for i in range(5):
		'''
		while this will only send 5 random mails
		you could tweak things probably using
		a while-loop, incase you just feel like
		you know being a jerk and all (lol..jk)'''
		text = '''
			 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut condimentum nisi at turpis pellentesque, ac dapibus augue eleifend. Nunc quis felis quis lorem iaculis dictum. Integer sit amet ultricies quam. Nam vel rhoncus arcu, vitae auctor ex. Phasellus lorem quam, feugiat aliquet rutrum id, pharetra vel tortor. Pellentesque sagittis est at suscipit rutrum. Nulla quis tempor felis. Sed eu tellus feugiat, sagittis elit ut, tincidunt ante. Aenean id elit justo. Ut consectetur luctus nunc ac mattis. Nullam at pharetra arcu. Aenean sodales nunc sed fringilla blandit. Suspendisse pretium mi at urna aliquam, non luctus enim congue. Duis vehicula, enim efficitur hendrerit posuere, mauris neque malesuada massa, venenatis blandit mi tellus in dolor. Aliquam erat volutpat.

Proin accumsan mi eu tempus mollis. Morbi id sodales quam, eu blandit leo. Nam convallis, nibh et semper feugiat, turpis dui pharetra mi, nec ultricies arcu lorem ac nibh. Curabitur sit amet purus id justo posuere mollis ut at sapien. Integer semper nec erat tincidunt tempus. Nunc mi velit, malesuada quis sapien id, porta hendrerit magna. Integer vel auctor libero. Vivamus ornare convallis convallis. Morbi porta odio vitae ex sollicitudin, id elementum risus laoreet. Proin interdum odio eget velit ultricies eleifend. Morbi id massa pulvinar, lacinia tellus id, mattis elit. Nullam vehicula, nisi ut placerat tempus, lectus enim convallis odio, pretium hendrerit lectus lorem nec massa. Mauris dapibus, magna quis malesuada tristique, turpis justo semper lorem, vitae dapibus lacus tortor a nunc. Suspendisse pellentesque libero eget velit rhoncus, non rhoncus ipsum aliquet. In hendrerit blandit ligula dictum pharetra. Maecenas ligula justo, euismod sed orci semper, lobortis hendrerit eros.  '''
		text = text.split()
		random.shuffle(text)
		text = ''.join(i + ' ' for i in text)
		msg = Message('',sender='paulcurious7@gmail.com',recipients=[email])
		msg.body = text
		mail.send(msg)
		time.sleep(frequency)
	return 'Message sent'

'''@app.route('/rec',methods=['GET','POST'])
def rec():
	#Get Data
	email = request.form['email']
	frequency = request.form['frequency']

	#create user_data
	newData = user_data(email,frequency)

	#Add to db
	db.session.add(newData)
	db.session.commit()

	return render_template('index.html')'''

if __name__ == '__main__':
	app.run(debug=True)

