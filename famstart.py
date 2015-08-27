from flask import Flask,render_template
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/famstart/')
def start(app='FamStart'):
    return render_template('famstart.html',app=app)
 
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')