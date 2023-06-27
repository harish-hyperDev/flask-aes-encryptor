from flask import Flask, render_template, request
from encrypt.encrypt import encryptor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():

	if request.method == 'POST':
		encrypted_text = encryptor(
							request.form['plain-text'], 
							request.form['plain-key']
						)
		return render_template(
						'index.html',
						txt=request.form['plain-text'],
						keyy=request.form['plain-key'],
						enc=encrypted_text
					)

	return render_template('index.html')