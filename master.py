
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


############# Functions ###############################################################

#Definition of the main function
def pageRank(links,iterations,epsilon,alpha):
    data = sc.textFile(inputFile,1)  
    links = data.map(lambda url: sep(url)).distinct().groupByKey().cache()
    it=0

    nb_nodes=links.distinct().count()
    
    ranks = links.map(lambda nb_neighbors: (nb_neighbors[0], 1/nb_nodes))  
    convergence_analyze=[]  
    stat = []
    
    for it in range(iterations) :
        
        contributions = links.join(ranks).flatMap( lambda url_rank: weight(url_rank[1][0], url_rank[1][1]))  
        ranks_update = contributions.reduceByKey(add).mapValues(lambda ranks: ranks * alpha + (1-alpha)/nb_nodes) 
        stat1 = ranks_update.distinct().count()
        stat.append(stat1)
        diff = ranks.join(ranks_update).map(lambda score : abs(score[1][1]-score[1][0])/score[1][0])
        list_diff_rank=diff.collect()       
        convergence_analyze.append(sum(i<epsilon for i in list_diff_rank)/len(list_diff_rank))
        ranks=ranks_update
        value = ranks.collect()    
        it+=1
        
    output=(ranks_update, convergence_analyze, value)
    return output
#Definition of the useful functions
def weight(url,rank):
    nb_url=len(url)
    for url in nb_url:
        yield (url,rank/nb_url)
 
def sep(url):
    separate = re.split(r'\t', url)
    return separate[0], separate[1]
#################### Application ###################################################
#Initialization of the parameters
alpha=0.85
epsilon=1e-3
iterations=10

#Dataset for natural graph
inputFile = "web-Stanford2.txt"
ranks_update,convergence_analyze, value, stat=pageRank(links,iterations,epsilon,alpha)

#Dataset for reverse graph
inputFile = "web-Stanford3.txt"
ranks_update_r,convergence_analyze_r, value_r, stat_r=pageRank(links,iterations,epsilon,alpha)

######################Description of the results####################################
#Top 10
df5 = pd.DataFrame(valeur)
df_sort_bis = df5.sort_values(by=1, ascending=False)
print(df_sort_bis[:10])

df6 = pd.DataFrame(valeur_r)
df_sort = df6.sort_values(by=1, ascending=False)
print(df_sort[:10])

df7 = pd.merge(df5, df6, on=0, how='outer')
df7.isnull().sum()

#Plots 
plt.plot(p_converge_r, "#dd1c77",label= "RPR")
plt.plot(p_converge, "#2b8cbe", label = "PR")
plt.ylabel('Percentage of convergence among pageranks')
plt.xlabel('Number of Iterations')
plt.legend()
plt.show()

plt.plot(stat_r, "#dd1c77",label= "RPR")
plt.plot(stat, "#2b8cbe", label = "PR")
plt.ylabel('Number of ranks')
plt.xlabel('Number of Iterations')
plt.show()
