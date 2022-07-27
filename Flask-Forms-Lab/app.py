from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = "icecream"

username = "little_capy"
password = "capybara809"
facebook_friends=["pastor-greg","fred09","xx.emo_kidYx", "perryringlet", "rustymetal", "that_one_guy_in_all_of_my_lessons"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html', wrong=False)
	else:
		form_username = request.form['username']
		form_password = request.form['password']
		print(form_username, form_password)
		if (form_username == username and form_password == password):
			return redirect(url_for('go_to_home'))
		else:
			return render_template('login.html', wrong=True)


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