
PageRank is an algorithm that was first developed by Google Search to rank websites. It considers that the interest of a site is directly proportional to its popularity, where the popularity is seen as the number of links which point towards him. In the article "Local Methods for Estimating PageRank values" (2004), the authors Y. Chen, Q. Gan and Suel present a way to adapt the idea of PageRank to a local estimation, enabling the estimation of the rank of pages that are part of a subgraph of the web. Based on this method, Z. Bar-Yossef and L.-T. Mashiach show that we can improve the results obtained by local approximation using reverse web graphs instead of natural graphs. They underline the fact that the reverse pagerank method is particulary strong in the case of graphs that have a lot of in-degrees in comparision to out-degrees. *(The in-degree of a node is the number of hyperlinks pointing to it)*.   
We will present briefly present the method of local approximation and show how we implemented it using MapReduce in the Python environment. 

## The dataset : the Subgraph of Stanford Website  
We used the graph extracted from the Stanford website. It is a page crawl of the www.stanford.edu domain performed in September 2002 by the WebBase project (http://snap.stanford.edu/data/web-Stanford.html). Nodes represent pages from Stanford University and directed edges represent hyperlinks between them.   
There are two columns. The first column shows the indexes of the URLs of Stanford website's pages. The second column has all the indexes of the URLs that we can go to from the first column web pages. We directly use this dataset to  approximate the local PageRank algorithm (erasing the first few lines that are a description of the dataset). We call this dataset "web-Stanford-natural.txt". Furthermore, we build a reversed graph based on the first one : we simple invert the order of the two columns of the dataset. The resulting graph is called "web-Stanford-reverse.txt".   
To account for the problem of nodes with out-degree zero, we prune the graph, that is we remove the leak nodes in the initial graph. Furthermore , we add a dampening factor alpha. We take the value commonly used, that is alpha = 0.85. 

## Methodologie 

We want to estimate the rank of the different webpages : 

![alt tag](https://github.com/eroblin/Reverse-PageRank/blob/master/equation.png )

We inititialize the rank of all webpages uniformly. We iterate and update the rank of the different webpages. 
We implement the algorithm using the Map and Reduce framework. Spark uses Resilient Distributed Datasets to operate on the data. RDDs support two types of operations: transformations *(lazy operations that return another RDD)* and actions *(operations that trigger computation and return values)*. 

## Results


