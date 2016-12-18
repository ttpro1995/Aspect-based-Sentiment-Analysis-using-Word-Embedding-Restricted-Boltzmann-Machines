#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Dai Nguyen'

#Thư viện
import gensim


if __name__ == "__main__":
    # Load file
    print "Loading file..."
    file_training = open('Training_word2vec_viet.TXT','r')
    sentences = file_training.readlines()

    # Huấn luyện mô hình Word2Vec cho tiếng Việt
    print "Splitting file..."
    for i in range(len(sentences)):
        sentences[i] = sentences[i].split()
    print sentences
    print "Training model..."
    model = gensim.models.word2vec.Word2Vec(sentences=sentences, size=300, window=5, min_count=1, workers=5)
    print "Save model..."
    model.save('Word2Vec_TiengViet.model')

    # Thử nha
    print model['quá']