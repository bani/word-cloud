#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
from collections import Counter

negative = ['and', 'the', 'to', 'of', 'i', 'it', 'use', 'a', '', 'is', 'that', 'its', 'my', 'for',
  'with', 'very', 'in', 'up', 'have', 'so', 'how', 'can', 'are', 'on', 'me', 'was', 'as', 'get',
  'all', 'set', 'not', 'your', 'really', 'an', 'be', 'has', 'but', 'make', 'we', 'do', 'from',
  'our', 'also', 'when', 'able', 'been', 'dont', 'out', 'or', 'at', 'this', 'am', 'than', 'by',
  'us', 'if', 'were', 'im', 'had']

def main(file, output):
  answers = open(file, 'r')
  words = []
  for line in answers:
    line = line.lower().replace('\r\n', '')
    line = re.sub(r'([^\sa-z]|_)+', '', line)
    words.extend(line.split(' '))
  answers.close()
  frequency = Counter(words)
  for word in negative:
    del frequency[word]
  wordcloud = ''
  for word in frequency.most_common(250):
    wordcloud += '<span data-weight="%d">%s</span>' % tuple(reversed(word))
  
  html = open(output, 'w')
  html.write(wordcloud)
  html.close()

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print 'Usage: /word_count.py <input file> <output file>'
    exit()
  main(sys.argv[1], sys.argv[2])

