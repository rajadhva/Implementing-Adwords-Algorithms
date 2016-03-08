__author__ = 'Vaibhav'

import xlrd
import csv
import random
import sys
f = open('queries.txt', 'r+')
queries=[]
for line in f:
    queries.append(line)
    print line

#c = csv.writer(open("bidder_dataset.csv", "wb"))


#making an advertiser query dictionary
cr = csv.reader(open("bidder_dataset.csv","rb"))

next(cr,None)
query_advertiser={}
advertiser_budget={}

for row in cr:
    if(query_advertiser.has_key(row[1])):
       query_advertiser[row[1]][row[0]]=row[2]
    else:
       query_advertiser[row[1]]={}
       query_advertiser[row[1]][row[0]]=row[2]

    if(row[3] not in (None, "")):
        advertiser_budget[row[0]]=row[3]


#for key in query_advertiser.keys():
    #print key,query_advertiser[key]

#for key in advertiser_budget.keys():
    #print key,advertiser_budget[key]


greedy_array=greedy(query_advertiser,advertiser_budget,queries)

def greedy(query_advertiser,advertiser_budget,queries):
    for i in range(0,100):
        random.seed(0)
        queries=random.shuffle(queries)
        current_budget=advertiser_budget
        for query in queries:
            advertisers=query_advertiser[query].keys()
            advertisers=filter(advertisers,current_budget)
            if not advertisers:
                continue
            max=-sys.maxint-1
            for


def filter(advertisers,current_budget):
    for name in advertisers:
        if(current_budget[advertisers]==0):
            advertisers.remove(name)

    return advertisers

def shuffle(temp3):
