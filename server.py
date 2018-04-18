#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, url_for, redirect, render_template
from data_munging import parseFile

app = Flask(__name__)
    
@app.route('/')
def root():
	return redirect('/section/0')
	
@app.route('/section/<index>')
def section(index):
	try:
		index = int(index)
	except ValueError:
		abort(404)
	
	vocab = parseFile()
	section = vocab[index]
	return render_template('section.html', 
		title=section.title, 
		entries=section.entries, 
		prev_href=url_for('section', index=(index - 1) % len(vocab)),
		next_href=url_for('section', index=(index + 1) % len(vocab)))

