from flask import Flask
from flask import request
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	nachricht = "Hallo Welt!"
	return render_template('index.html', nachricht=nachricht) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')

