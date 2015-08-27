from flask import Flask,render_template
app = Flask(__name__)

@app.route('/famstart/')
def start(app='FamStart'):
    return render_template('famstart.html',app=app)
 
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')