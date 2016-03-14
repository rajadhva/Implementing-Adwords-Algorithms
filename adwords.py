__author__ = 'Vaibhav'

#import xlrd
import csv
import random
import sys
import operator
f = open('queries.txt', 'r+')
optimal_revenue=0.0
queries=[]
for line in f:
    queries.append(line.rstrip())
    #print line



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

    #print advertiser_budget
#for key1 in query_advertiser.keys():
            #print query_advertiser[key1]

#for i in advertiser_budget.keys():
    #print str(i) + " : " + str(advertiser_budget[i])

#for key in query_advertiser.keys():
    #print key,query_advertiser[key]

#for key in advertiser_budget.keys():
    #print key,advertiser_budget[key]

for i in advertiser_budget.values():
    optimal_revenue= optimal_revenue + i


def greedy(query_advertiser,advertiser_budget,queries):

    revenue=[]
    main_revenue=0
    flag=False

    for i in range(100):
        if(i!=0):
            random.seed(0)
            random.shuffle(queries)
        #print advertiser_budget
        current_budget=advertiser_budget.copy()
        temp_revenue=0
        for query in queries:
            advertisers=query_advertiser[query].keys()

            if not advertisers:
                continue
            max=0
            temp_advertiser = -1
            #print sorted(advertisers)
            for advertiser in sorted(advertisers):
                if current_budget[advertiser] - query_advertiser[query][advertiser] > 0:
                    if(query_advertiser[query][advertiser] > max):
                        max=query_advertiser[query][advertiser]
                        temp_advertiser= advertiser
            if temp_advertiser != -1:            
                current_budget[temp_advertiser] = current_budget[temp_advertiser] - max
                temp_revenue= temp_revenue + max
        revenue.append(temp_revenue)
    print revenue
    print current_budget
    average_revenue=0
    for i in revenue:
        average_revenue= average_revenue+i

    return main_revenue,average_revenue/100



def filter(advertisers,current_budget,query_advertiser,query):
    for name in advertisers:
        if(current_budget[name]==0 or current_budget[name]-query_advertiser[query][name]<0):
            advertisers.remove(name)

    return advertisers



def balance(query_advertiser,advertiser_budget,queries):
    revenue=[]
    main_revenue=0
    for i in range(100):
        if(i!=0):
            random.seed(0)
            random.shuffle(queries)
        #print advertiser_budget
        current_budget=advertiser_budget.copy()
        temp_revenue=0
        for query in queries:
            advertisers=query_advertiser[query].keys()

            for advertiser in advertisers:
                if(current_budget[advertiser]==0):
                    print "Came Here"
                    advertiser.remove(advertiser)
            if not advertisers:
                continue
            max=0
            temp_advertiser = -1
            for advertiser in advertisers:
                if current_budget[advertiser] - query_advertiser[query][advertiser] > 0:
                    if(current_budget[advertiser]>max):
                        max=current_budget[advertiser]
                        temp_advertiser=advertiser
            if temp_advertiser != -1:
                current_budget[temp_advertiser] = current_budget[temp_advertiser] - query_advertiser[query][temp_advertiser]
                temp_revenue= temp_revenue + query_advertiser[query][temp_advertiser]
        revenue.append(temp_revenue)
    print revenue
    print current_budget
    average_revenue=0
    for i in revenue:
        average_revenue= average_revenue+i

    return main_revenue,average_revenue/100


#driver functions to fetch output and print them:
def greedyOutput():
   main_revenue,average_revenue=greedy(query_advertiser,advertiser_budget,queries)
   #print optimal_revenue
   print "The revenue in greedy is" + " : " + str(average_revenue)
   print "The competitive ratio in greedy is" + " : " + str(average_revenue/optimal_revenue)

def balanceoutput():
   main_revenue,average_revenue=balance(query_advertiser,advertiser_budget,queries)
   #print optimal_revenue
   print "The revenue in balance is" + " : " + str(average_revenue)
   print "The competitive ratio in balance is" + " : " + str(average_revenue/optimal_revenue)


greedyOutput()
balanceoutput()



