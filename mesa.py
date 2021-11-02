from flask import Flask, render_template


app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newt.html')
def newt():
    return render_template('newt.html')

@app.route('/newhu.html')
def newhu():
    return render_template('newhu.html')

@app.route('/newhe.html')
def newhe():
    return render_template('newhe.html')

if __name__ == '__main__':
   app.run(debug=True)

