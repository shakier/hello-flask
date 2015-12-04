from flask import Flask, render_template, request, redirect
# edit this file to add functionality for stock ticker project
# to debug locally:
# http://127.0.0.1:33507


app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
