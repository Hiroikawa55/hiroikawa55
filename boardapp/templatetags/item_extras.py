from django import template # 追記 必須
from django.template.defaultfilters import stringfilter
from boardapp.forms import FindForm
from pprint import pprint
import re

register = template.Library() # 追記 必須

@register.filter(name='myfilter')
@stringfilter
def myfilter(value):
    return value.split('。')

@register.filter
@stringfilter
def filter_age(value1, value2):
    s = value1
    f = '\n'.join(s.splitlines())
    s_l = f.split('。')
    word = str(value2)
    for i in s_l:
        if word in i:
            return i

@register.filter
@stringfilter
def filter_age2(value1, value2):
    s = value1
    g = '\n'.join(s.splitlines())
    f = g.replace("\u3000","")
    f = f.replace("\t","")
    s_l = f.split('。')
    word = str(value2)
    d = []
    for i in s_l:
        if word in i:
            d.append(i)
    return d

from sklearn.metrics.pairwise import cosine_similarity
from janome.tokenizer import Tokenizer
import MeCab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

@register.filter
@stringfilter

def filter_near(value1, value2):
    tagger = MeCab.Tagger("-Owakati")
    value3 = str(value1)
    docs = value3.splitlines()
    value4 = str(value2)
    docs = [tagger.parse(sentence).strip() for sentence in docs]
    vectorizer = CountVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
    transformer = TfidfTransformer()
    tf = vectorizer.fit_transform(docs)  # 単語の出現頻度を計算
    tfidf = transformer.fit_transform(tf)  # 各ドキュメントのtfidfを計算
    sample_tf = vectorizer.transform([tagger.parse(value4).strip()])
    sample_tfidf = transformer.transform(sample_tf)
    similarity = cosine_similarity(sample_tfidf, tfidf)[0]
    if similarity > 0.6:
        topn_indices = np.argsort(similarity)[::-1][:3]
        for sim, tweet in zip(similarity[topn_indices], np.array(docs)[topn_indices]):
            return sim, "".join(tweet.split())

@register.filter
@stringfilter
def ppri(value):
    pprint(value)

@register.filter(name='cut')
@stringfilter
def cut(value, arg):
    "入力から arg の値を全て取り去る"
    return value.replace(arg, '')