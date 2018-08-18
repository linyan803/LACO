#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# -2018.8.18 -Peter Lee

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def entry_page():
    return render_template('entry.html',
                           the_title="Welcome Peter Lee")


app.run()
