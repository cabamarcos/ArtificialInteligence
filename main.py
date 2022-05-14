# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import csv




text = ''
csvreader = csv.reader(open(r'C:/Users/migue/Data.csv'))
ListOfWords = []
sum1 = 0
words = []
for i in csvreader:
    for string in i:
        for letter in string:
            if letter == 'N' or letter == 'E' or letter == 'W':
                words.append(text)
                text = letter
                words.append(text)
                text = ''
            elif letter ==';':
                pass
            else:
                text+=letter
        words.append(text)
        ListOfWords.append(text)
        text = ''
        words = []
    sum1 += 1



