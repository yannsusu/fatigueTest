from flask import Flask
from flask import request, session, redirect, url_for



app = Flask(__name__)
app.secret_key = 'qwerty1234567890'



@app.route('/', methods=['GET', 'POST'])
def index():

	strHtml = '<a href="/protected">Protected</a> | <a href="/logout">Logout</a><br/><br/>'

	if request.method == 'GET':
				
		strHtml = strHtml + '<form method="post" action="/">'
		strHtml = strHtml + '<label for="email">Email</label> <input type="text" id="email" name="email" /><br/>'
		strHtml = strHtml + '<label for="password">Password</label> <input type="password" id="password" name="password" /><br/>'
		strHtml = strHtml + '<input type="reset" /> <input type="submit" />'
		strHtml = strHtml + '</form>'	
		
	elif request.method == 'POST':
		
		print('Login: email={}, password={}'.format(request.form['email'], request.form['password']))
		
		session['isLogin'] = True
		session['email'] = request.form['email']
		strHtml += 'Login successfully!'
	
	else:
		
		strHtml += 'Unsupported HTTP Method'
	
	return strHtml



@app.route('/protected', methods=['GET'])
def protected():

	strHtml = '<a href="/protected">Protected</a> | <a href="/logout">Logout</a><br/><br/>'

	if 'isLogin' in session and session['isLogin'] == True:
	
		strHtml = strHtml + 'You are login as ' + session['email']
	
	else:
	
		strHtml = strHtml +  'You are not login'
		
	return strHtml



@app.route('/logout', methods=['GET'])
def logout():
	
	session.pop('isLogin', None)
	session.pop('email', None)
	
	return redirect(url_for('index'))
