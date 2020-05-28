import warnings
warnings.filterwarnings("ignore")

#-*- coding:utf-8 _*-
import codecs
import re
from model  import  HMM
from dataset import  dataset
import os

input_data = codecs.open('train_ner.txt','r','utf-8')

for line in input_data.readlines():
    print('line:',line)
    simple = re.compile("[[](.*?)[]]dis{1}").findall(line)
    for word in simple:
        word = word.strip().split()
        print('word list:',word)
        for word in simple:
            if len(word) < 10:
                word = word.strip().split()
                if len(word) == 1:
                    print(word[0] + "\tB-dis\n")
                else:
                    print(word[0] + "\tB-dis\n")
                    for w in range(1, len(word)):
                        print(word[w] + "\tI-dis\n")
