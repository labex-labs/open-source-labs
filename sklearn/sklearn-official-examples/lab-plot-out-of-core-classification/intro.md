# Introduction

This lab provides an example of how to use scikit-learn for text classification using out-of-core learning. The goal is to learn from data that does not fit into main memory. To achieve this, we make use of an online classifier that supports the partial_fit method, which will be fed with batches of examples. To ensure that the feature space remains the same over time, we leverage a HashingVectorizer that will project each example into the same feature space. This is especially useful in the case of text classification where new features (words) may appear in each batch.

> You can write code in `plot-out-of-core-classification.ipynb`.
