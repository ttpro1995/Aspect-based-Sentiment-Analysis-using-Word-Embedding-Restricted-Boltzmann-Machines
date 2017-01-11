
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from collections import defaultdict


# 1190
# label:
# FOOD
# STAFF
# AMBIENCE
# SERVICE
# OTHERS

# counting aspect freq
# counting polarity freq


def InspectData (filename):
    file = open(filename,'r')
    data= file.read()
    soup = BeautifulSoup(data, 'xml')
    all_sentences = soup.find_all('sentence')
    all_aspects = []
    all_labels = [''] * len(all_sentences)
    posneg_labels = []

    aspects_freq = defaultdict()
    aspects_freq["FOOD", "positive"] = 0
    aspects_freq["AMBIENCE", "positive"] = 0
    aspects_freq["STAFF", "positive"] = 0
    aspects_freq["PRICE", "positive"] = 0
    aspects_freq["SERVICE", "positive"] = 0
    aspects_freq["OTHER", "positive"] = 0

    aspects_freq["FOOD", "negative"] = 0
    aspects_freq["AMBIENCE", "negative"] = 0
    aspects_freq["STAFF", "negative"] = 0
    aspects_freq["PRICE", "negative"] = 0
    aspects_freq["SERVICE", "negative"] = 0
    aspects_freq["OTHER", "negative"] = 0

    aspects_freq["FOOD", "neutral"] = 0
    aspects_freq["AMBIENCE", "neutral"] = 0
    aspects_freq["STAFF", "neutral"] = 0
    aspects_freq["PRICE", "neutral"] = 0
    aspects_freq["SERVICE", "neutral"] = 0
    aspects_freq["OTHER", "neutral"] = 0

    num_of_label = 0 # a pair of aspects_sentiment
    num_of_sentence = len(all_sentences)
    num_aspect_per_sent = defaultdict()


    # Tìm aspect cho các câu đó
    for i in range(len(all_sentences)):
        if ('<Opinions>' in str(all_sentences[i])):
            Opinions = all_sentences[i].Opinions.find_all('Opinion')
            aspects = ''
            sentiments = ''
            if (len(Opinions) not in num_aspect_per_sent.keys()):
                num_aspect_per_sent[len(Opinions)] = 1
            else:
                num_aspect_per_sent[len(Opinions)] +=1
            if (len(Opinions) > 50):
                print all_sentences[i]

            for j in range(len(Opinions)):
                num_of_label+=1
                aspect = Opinions[j]['category']
                sentiment = Opinions[j]['polarity']
                if ('FOOD' in aspect):
                    aspects_freq['FOOD',sentiment] += 1
                if ('AMBIENCE' in aspect):
                    aspects_freq['AMBIENCE',sentiment]+= 1
                if ('STAFF' in aspect):
                    aspects_freq['STAFF',sentiment] += 1
                if ('PRICE' in aspect):
                    aspects_freq['PRICE',sentiment] += 1
                if ('SERVICE' in aspect):
                    aspects_freq['SERVICE',sentiment] += 1
                if ('OTHER' in aspect):
                    aspects_freq['OTHER',sentiment] += 1

    return aspects_freq, num_of_sentence, num_of_label,num_aspect_per_sent

aspects_freq, num_of_sentence, num_of_label, num_aspect_per_sent = InspectData('../_Data/Output.xml')
print('breakpoint')