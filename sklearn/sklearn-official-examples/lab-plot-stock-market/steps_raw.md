# Visualizing Stock Market Structure

## Introduction

In this lab, we will use several unsupervised learning techniques to extract the structure of the stock market from variations in historical quotes. We will use the daily variation in quote price to find which quotes are correlated conditionally on the others. Then, we will use clustering to group together quotes that behave similarly. Finally, we will lay out the different symbols on a 2D canvas using manifold techniques to retrieve 2D embedding.

## Steps

### Step 1: Retrieve the data from Internet

The data is from 2003 - 2008. This is reasonably calm and can be obtained from APIs like the `data.nasdaq.com` and `alphavantage.co`.

### Step 2: Learning a graph structure

We use sparse inverse covariance estimation to find which quotes are correlated conditionally on the others. Specifically, sparse inverse covariance gives us a graph, that is a list of connections. For each symbol, the symbols that it is connected to are those useful to explain its fluctuations.

### Step 3: Clustering using affinity propagation

We use clustering to group together quotes that behave similarly. Here, we use affinity_propagation as it does not enforce equal-size clusters, and it can choose automatically the number of clusters from the data.

### Step 4: Embedding in 2D space

For visualization purposes, we need to lay out the different symbols on a 2D canvas. For this we use manifold techniques to retrieve 2D embedding.

### Step 5: Visualization

The output of the 3 models are combined in a 2D graph where nodes represents the stocks and edges the cluster labels are used to define the color of the nodes. The sparse covariance model is used to display the strength of the edges, and the 2D embedding is used to position the nodes in the plan.

## Summary

In this lab, we used unsupervised learning techniques to extract the structure of the stock market from variations in historical quotes. We learned how to retrieve the data, learn a graph structure, cluster using affinity propagation, embedding in 2D space, and finally, visualize the output of the 3 models in a 2D graph.
