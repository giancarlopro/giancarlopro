from flask import Flask, send_file
from os import listdir
from os.path import isfile, join, realpath, dirname
from random import choice


app = Flask(__name__)

def get_gif():
    base = dirname(realpath(__file__)) + '/gif/'
    return choice([join(base, f) for f in listdir(base) if isfile(join(base, f))])

@app.route('/image.gif')
def gif():
    return send_file(get_gif(), mimetype='image/gif')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    response.cache_control.no_cache = True
    return response

if __name__ == '__main__':
    app.run()
