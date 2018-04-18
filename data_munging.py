#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

class Entry:
    def __init__(self, word, gloss):
        self.word = word
        self.gloss = gloss
        
    def __repr__(self):
        return '{} {}'.format(self.word, self.gloss)
        
class Section:            
    def __init__(self, title):
        self.title = title
        self.entries = []
        
    def __repr__(self):
        return '{}\n  '.format(self.title) + '\n  '.join([str(word) for word in self.entries])
    
def parseFile():
    vocabObj = []
    
    tree = ET.parse('Basics of Biblical Hebrew.xml')
    root = tree.getroot()
    for section in root:
        sectionTitle = section.find('title').text
        sectionObj = Section(sectionTitle)
        vocabObj.append(sectionObj)
        for entry in section.iterfind('entry'):
            word = entry.find('word').text
            gloss = entry.find('gloss').text
            sectionObj.entries.append(Entry(word, gloss))
    
    return vocabObj
    
def main():
    vocabObj = parseFile()
    print('\n'.join([str(section) for section in vocabObj]))

if __name__ == '__main__':
    import sys
    sys.exit(main())
