
PageRank is an algorithm that was first developed by Google Search to rank websites. It considers that the interest of a site is directly proportional to its popularity, where the popularity is seen as the number of links which point towards him. In the article "Local Methods for Estimating PageRank values" (2004), the authors Y. Chen, Q. Gan and Suel present a way to adapt the idea of PageRank to a local estimation, enabling the estimation of the rank of pages that are part of a subgraph of the web. Based on this method, Z. Bar-Yossef and L.-T. Mashiach show that we can improve the results obtained by local approximation using reverse web graphs instead of natural graphs. 
We will present briefly the method of local approximation and show how we implemented it using MapReduce in the Python environment. 

# The dataset : the Subgraph of Stanford Website  
