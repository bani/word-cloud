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
  singular_rules = [lambda w: w[-3:] == 'ies' and w[:-3] + 'y',
                    lambda w: w[-4:] == 'ives' and w[:-4] + 'ife',
                    lambda w: w[-3:] == 'ves' and w[:-3] + 'f',
                    lambda w: w[-2:] == 'es' and w[:-2],
                    lambda w: w[-1:] == 's' and w[:-1],
                    lambda w: w,
                    ]
  words = [[f(word) for f in singular_rules if f(word) is not False][0] for word in words]
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

