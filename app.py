from flask import Flask, render_template
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output

app = Flask(__name__ , template_folder='templates')

@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html')

@app.route("/indeed",methods=['GET', 'POST'])
def indeed():
    cmd = subprocess.Popen('cmd.exe /K cd C:\\Users\\nciba\\PycharmProjects\\pythonProject\\indeed && scrapyrt -p 3001')
    cmd = subprocess.communicate()
@app.route("/linkedin",methods=['GET','POST'])
def linkedin():
    cmd = subprocess.Popen('cmd.exe /K cd C:\\Users\\nciba\\PycharmProjects\\pythonProject\\jobSpider && scrapyrt -p 3000')
    cmd = subprocess.communicate()
if __name__ == '__main__':
    app.run(debug= True,port=5000)
