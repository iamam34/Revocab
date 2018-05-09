#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET

class Entry:
    def __init__(self, word, gloss):
        self.word = word
        self.gloss = gloss
        
    def __repr__(self):
        return u'{} {}'.format(self.word, self.gloss, encoding='utf8')
        
class Section:            
    def __init__(self, title):
        self.title = title
        self.entries = []
        
    def __repr__(self):
        return u'{}\n  '.format(self.title) + u'\n  '.join([unicode(word) for word in self.entries])
    
def parseFile():
    vocabObj = []
    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Basics of Biblical Hebrew.xml')
    tree = ET.parse(filename)
    root = tree.getroot()

    for section in root:
        sectionTitle = section.find('title').text
        sectionObj = Section(sectionTitle)
        vocabObj.append(sectionObj)
        for entry in section.iterfind('entry'):
            word = entry.find('word').text
            gloss = [g.text for g in entry.findall('gloss')]
            sectionObj.entries.append(Entry(word, gloss))
    
    return vocabObj
    
def main():
    vocabObj = parseFile()
    print(u'\n'.join([unicode(section) for section in vocabObj]))

if __name__ == '__main__':
    import sys
    sys.exit(main())
