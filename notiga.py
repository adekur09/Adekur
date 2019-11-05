# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:21:07 2019

@author: asus
"""


import tweepy
import pandas
from tweepy import OAuthHandler, Stream, StreamListener
import csv

n=int(input("masukkan jumlah topik = "))
topik=[]
for i in range (n):
    temp=str(input("masukkan topik ke-{} = ".format(i+1)))
    topik.append(temp)


consumer_key="X2VfS0ODunWQ5IdmwJcQvrxdS"
consumer_secret="XTI3GGAU4r7xr6gELJaUfSKVQLuwRwI0PLRefIFRdINlE6rRI9"
access_token="2297856090-IRjQiWflrYPxkfHaR7Js1m8SBQOdL5cNUaA2Twm"
access_token_secret="Y3KtjH5BEraAbOCeDh51Lh68NOESbGTDaa0qp3OU4vtfP"
auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


list0=[]
list1=[]
for i in range (n):
    for tweet in tweepy.Cursor(api.search,q="#"+topik[i],count=5,
                           lang="id").items():
        list0.append(tweet._json)
    data=pandas.DataFrame(list0)
    data1=data[['text','created_at']].head()
    print('\n',"======================================",topik[i],"======================================")
    print('\n',data1)
#    list1.append(data1)
#results=list1
#print(results)
#export_csv = results.to_csv (r'F:\dokumen\FGA BD\export_dataframe3.csv', header=True)
#print("")
#print("EXPORT TO CSV SUCCESS!!!")
#print(data1)