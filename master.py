
#Definition of the SparkContext 
#Use of two cores (master local[2]) corresponding of the number of cores of the computer
sparkConf = SparkConf().setAppName("PageRank")   
sc = SparkContext.getOrCreate()

#Installation of the packages
import os
os.chdir("C:/Users/Elvire/Desktop/spark/")
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
%matplotlib inline
from operator import add
import numpy as np
import re
import sys

#Description of the data

#Definition of the useful functions
def weight(url,rank):
    nb_url=len(url)
    for url in nb_url:
        yield (url,rank/nb_url)
 
def sep(url):
    separate = re.split(r'\t', url)
    return separate[0], separate[1]

#Definition of the main function
def pageRank(links,iterations,epsilon,alpha):
    it=0
    
    nb_nodes=links.distinct().count()
    
    ranks = links.map(lambda nb_neighbors: (nb_neighbors[0], 1/nb_nodes))  
    convergence_analyze=[]  
    
    while it<iterations :
        
        contributions = links.join(ranks).flatMap( lambda url_rank: weight(url_rank[1][0], url_rank[1][1]))  
        ranks_update = contributions.reduceByKey(add).mapValues(lambda ranks: ranks * alpha + (1-alpha)/nb_nodes) 
        diff = ranks.join(ranks_update).map(lambda score : abs(score[1][1]-score[1][0])/score[1][0])
        list_diff_rank=diff.collect()       
        convergence_analyze.append(sum(i<epsilon for i in list_diff_rank)/len(list_diff_rank))
        ranks=ranks_update
        value = ranks.collect()    
        it+=1
        
    output=(ranks_update, convergence_analyze, value)
    return output
  
#Initialization of the parameters
alpha=0.85
epsilon=1e-3
iterations=20

#Dataset for natural graph
inputFile = "web-Stanford2.txt"
data = sc.textFile(inputFile,1)  
links = data.map(lambda url: sep(url)).distinct().groupByKey().cache()
ranks_update,convergence_analyze, value=pageRank(links,iterations,epsilon,alpha)

#Dataset for reverse graph
inputFile = "web-Stanford3.txt"
data = sc.textFile(inputFile,1)  
links = data.map(lambda url: sep(url)).distinct().groupByKey().cache()
ranks_update_r,convergence_analyze_r, value_r=pageRank(links,iterations,epsilon,alpha)

#Description of the results
