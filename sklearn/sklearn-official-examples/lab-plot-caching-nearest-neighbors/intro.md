# Introduction

This lab demonstrates how to precompute the k nearest neighbors before using them in KNeighborsClassifier. KNeighborsClassifier can compute the nearest neighbors internally, but precomputing them can have several benefits, such as finer parameter control, caching for multiple use, or custom implementations. Here we use the caching property of pipelines to cache the nearest neighbors graph between multiple fits of KNeighborsClassifier.

You can open the `plot-caching-nearest-neighbors.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)

We can not verify your answers automatically in this lab.
