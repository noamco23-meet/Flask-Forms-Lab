from fileinput import filename
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
import random
from werkzeug.utils import secure_filename
import os

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = "icecream"



#user info
username = "little_capy"
password = "capybara809"
facebook_friends=["pastor-greg","fred09","xx.emo_kidYx", "perryringlet", "rustymetal", "that_one_guy_in_all_of_my_lessons"]


#image requirements and setup
UPLOAD_FOLDER = "/home/student/Documents/MEET Summer Y2/Computer Science/Labs/Flask-Forms-Lab/Flask-Forms-Lab/images"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file is not None and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('login'))
		else:
			return redirect(url_for('login'))
	else:
		return render_template("upload.html")
	


@app.route('/login', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html', wrong=False)
	else:
		form_username = request.form['username']
		form_password = request.form['password']
		if (form_username == username and form_password == password):
			return redirect(url_for('go_to_home'))
		else:
			return render_template('login.html', wrong=True, image=filename)


@app.route('/home')
def go_to_home():
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def go_to_friendexists(name):
	if request.method == 'GET':
		is_friend = "not"
		if name in facebook_friends:
			is_friend = ""
		return render_template('/friend_exists.html', name=name, is_friend=is_friend)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)