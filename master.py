
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

#Definition of the main function

#Initialization of the parameters

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
