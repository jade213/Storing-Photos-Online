from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return 'hello world'

if __name__ == '__main__':
    start()