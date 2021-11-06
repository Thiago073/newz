from flask import Flask, render_template


app = Flask(__name__, template_folder='template')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index.html')
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

@app.route('/artigos.html')
def artigos():
    return render_template('artigos.html')

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/criar.html')
def criar():
    return render_template('criar.html')

if __name__ == '__main__':
   app.run(debug=True)

