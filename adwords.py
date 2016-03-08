__author__ = 'Vaibhav'

import xlrd
import csv
import random
import sys

f = open('queries.txt', 'r+')
queries=[]
for line in f:
    queries.append(line.rstrip())
    print line

#c = csv.writer(open("bidder_dataset.csv", "wb"))


#making an advertiser query dictionary
cr = csv.reader(open("bidder_dataset.csv","rb"))

next(cr,None)
query_advertiser={}
advertiser_budget={}

for row in cr:
    if(query_advertiser.has_key(row[1])):
       query_advertiser[row[1]][row[0]]=float(row[2])
    else:
       query_advertiser[row[1]]={}
       query_advertiser[row[1]][row[0]]=float(row[2])

    if(row[3] not in (None, "")):
        advertiser_budget[row[0]]=float(row[3])


#for key in query_advertiser.keys():
    #print key,query_advertiser[key]

#for key in advertiser_budget.keys():
    #print key,advertiser_budget[key]




def greedy(query_advertiser,advertiser_budget,queries):
    revenue=0
    #random.seed(0)
    #random.shuffle(queries)
    current_budget=advertiser_budget

    for query in queries:
        print query
        advertisers=query_advertiser[query].keys()
        advertisers=filter(advertisers,current_budget,query_advertiser,query)
        if not advertisers:
            continue
        max=-sys.maxint-1
        for advertiser in advertisers:
            if(query_advertiser[query][advertiser] > max):
                max=query_advertiser[query][advertiser]
                temp_advertiser=advertiser
            if(query_advertiser[query][advertiser]>max):
                if(advertiser<temp_advertiser):
                    max=query_advertiser[query][advertiser]
                    temp_advertiser=advertiser
        current_budget[temp_advertiser]= current_budget[temp_advertiser]-max
        revenue=revenue+max
    return revenue

def filter(advertisers,current_budget,query_advertiser,query):
    for name in advertisers:
        if(current_budget[name]==0 or current_budget[name]-query_advertiser[query][name]<0):
            advertisers.remove(name)

    return advertisers

print greedy(query_advertiser,advertiser_budget,queries)