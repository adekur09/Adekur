# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:00:24 2019

@author: asus
"""

import tweepy
import pandas
from tweepy import OAuthHandler, Stream, StreamListener
import datetime

topik=str(input("masukkan topik ke-1 = "))
topik1=str(input("masukkan topik ke-2 = "))
topik2=str(input("masukkan topik ke-3= "))
topik3=str(input("masukkan topik ke-4= "))
topik4=str(input("masukkan topik ke-5= "))

consumer_key="X2VfS0ODunWQ5IdmwJcQvrxdS"
consumer_secret="XTI3GGAU4r7xr6gELJaUfSKVQLuwRwI0PLRefIFRdINlE6rRI9"
access_token="2297856090-IRjQiWflrYPxkfHaR7Js1m8SBQOdL5cNUaA2Twm"
access_token_secret="Y3KtjH5BEraAbOCeDh51Lh68NOESbGTDaa0qp3OU4vtfP"
auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


list0=[]
for tweet in tweepy.Cursor(api.search,q=topik,count=5,lang="id").items():
    list0.append(tweet._json)
    
list1=[]
for tweet in tweepy.Cursor(api.search,q=topik1,count=5,lang="id").items():
    list1.append(tweet._json)
    
list2=[]
for tweet in tweepy.Cursor(api.search,q=topik2,count=5,lang="id").items():
    list2.append(tweet._json)
    
list3=[]
for tweet in tweepy.Cursor(api.search,q=topik3,count=5,lang="id").items():
    list3.append(tweet._json)

list4=[]
for tweet in tweepy.Cursor(api.search,q=topik4,count=5,lang="id").items():
    list4.append(tweet._json)

data=pandas.DataFrame(list0)
data1=data[['created_at','text']].head()
#print(data1)

data1=pandas.DataFrame(list1)
data11=data1[['created_at','text']].head()
#print(data11)

data2=pandas.DataFrame(list2)
data12=data2[['created_at','text']].head()
#print(data12)

data3=pandas.DataFrame(list3)
data13=data3[['created_at','text']].head()
#print(data13)

data4=pandas.DataFrame(list4)
data14=data4[['created_at','text']].head()
#print(data14)

frames=data
results=pandas.concat(data,data11,data12,data13,data14)
print(results)