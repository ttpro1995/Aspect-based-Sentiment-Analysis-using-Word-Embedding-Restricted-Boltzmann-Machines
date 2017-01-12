#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Dai Nguyen'

# Script chạy với anaconda

#Thư viện
import numpy as np
import operator
from bs4 import BeautifulSoup
import gensim
from scipy import spatial
from nltk.corpus import stopwords

# Hàm load dữ liệu
def LoadData (filename):
    file = open(filename,'r')
    data= file.read()
    soup = BeautifulSoup(data, 'xml')
    all_sentences = soup.find_all('sentence')
    all_aspects = []
    all_labels = [''] * len(all_sentences)
    posneg_labels = []

    # Tìm aspect cho các câu đó
    for i in range(len(all_sentences)):
        if ('<Opinions>' in str(all_sentences[i])):
            Opinions = all_sentences[i].Opinions.find_all('Opinion')
            aspects = ''
            sentiments = ''
            for j in range(len(Opinions)):
                aspect = Opinions[j]['category']
                sentiment = Opinions[j]['polarity']
                aspects += ' ' + aspect
                sentiments += ' ' + sentiment
            all_aspects.append(aspects)
            posneg_labels.append(sentiments)
        else:
            all_aspects.append('Others')
            posneg_labels.append('Others')
    # Có nhãn rồi chuyển nó sang labels (dạng số) được quy định như trên
    for i in range(len(all_sentences)):
        if ('FOOD' in all_aspects[i]):
            all_labels[i] += ' 1'
        if ('AMBIENCE' in all_aspects[i]):
            all_labels[i] += ' 3'
        if ('STAFF' in all_aspects[i]):
            all_labels[i] += ' 5'

    all_posneg_labels = [0]*len(posneg_labels)
    for i in range(len(all_sentences)):
        if ('negative' in posneg_labels[i] and 'positive' in posneg_labels[i]):
            all_posneg_labels[i] = 2
        elif ('positive' in posneg_labels[i]):
            all_posneg_labels[i] = 0
        elif ('negative' in posneg_labels[i]):
            all_posneg_labels[i] = 1

    # Tìm ra những câu chỉ nói về food staff hoặc ambience
    data = []
    labels = []
    posnegs = []
    for i in range(len(all_sentences)):
        if (all_labels[i] == ' 1'):
            text = all_sentences[i].text
            label = 1
            data.append(text)
            labels.append(label)
            posnegs.append(all_posneg_labels[i])
        if (all_labels[i] == ' 5'):
            text = all_sentences[i].text
            label = 5
            data.append(text)
            labels.append(label)
            posnegs.append(all_posneg_labels[i])
        if (all_labels[i] == ' 3'):
            text = all_sentences[i].text
            label = 3
            data.append(text)
            labels.append(label)
            posnegs.append(all_posneg_labels[i])
    return data, labels, posnegs

if __name__ == "__main__":
    # Load dữ liệu sentences
    print "Loading Data..."
    # Load dữ liệu
    data, labels, pos_neg_labels = LoadData('..\_Data\Output_FSA.xml')
    print len(data)
    # Ghi ra file
    file_out = open('svm_data.txt','w')
    for i in range(len(data)):
        data[i] = data[i].strip()
        file_out.write(data[i].encode('utf-8') + '\n')

    file_out = open('svm_labels.txt','w')
    for i in range(len(labels)):
        file_out.write(str(labels[i]) + '\n')

    file_out = open('svm_sentiment_labels.txt','w')
    for i in range(len(pos_neg_labels)):
        file_out.write(str(pos_neg_labels[i]) + '\n')