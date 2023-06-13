# Introduction

This lab demonstrates how to precompute the k nearest neighbors before using them in KNeighborsClassifier. KNeighborsClassifier can compute the nearest neighbors internally, but precomputing them can have several benefits, such as finer parameter control, caching for multiple use, or custom implementations. Here we use the caching property of pipelines to cache the nearest neighbors graph between multiple fits of KNeighborsClassifier.

> You can write code in `lab.ipynb`.
