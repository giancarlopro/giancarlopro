from flask import Flask, send_file
from os import listdir
from os.path import isfile, join, realpath, dirname
from random import choice

app = Flask(__name__)

def get_gif():
    base = dirname(realpath(__file__)) + '/gif/'
    return choice([join(base, f) for f in listdir(base) if isfile(join(base, f))])

@app.route('/gif')
def gif():
    return send_file(get_gif())

if __name__ == '__main__':
    app.run()
