#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import codecs
from jinja2 import Environment, FileSystemLoader, select_autoescape
from data_munging import parseFile
import shutil
import os

'''
make directories recursively if they don't already exist, else do nothing
copied from https://stackoverflow.com/a/600612/1925961
'''
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError, exc:
        if exc.errno == 17 and os.path.isdir(path): #EEXIST
            pass
        else:
            raise

def generate_sections(environment, vocab, filepath):
    template = environment.get_template('section.html')

    mkdir_p(filepath)

    for index, section in enumerate(vocab):
        page = template.render( 
            title=section.title, 
            entries=section.entries, 
            prev_href='./{0}.html'.format((index - 1) % len(vocab)),
            next_href='./{0}.html'.format((index + 1) % len(vocab)))
        filename = filepath + '/{}.html'.format(index)
        with codecs.open(filename, 'w', 'utf-8') as destination:
            print(page, file=destination)

def generate_overview(environment, vocab, filepath):
    template = environment.get_template('overview.html')
    mkdir_p(filepath)

    page = template.render( 
        title='Revocab', 
        entries=[entry for section in vocab for entry in section.entries])
    filename = filepath + '/overview.html'
    with codecs.open(filename, 'w', 'utf-8') as destination:
        print(page, file=destination)

def main():
    environment = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml']))

    vocab = parseFile()
    
    #generate_sections(environment, vocab, './static')

    generate_overview(environment, vocab, './static')

if __name__ == '__main__':
    main()