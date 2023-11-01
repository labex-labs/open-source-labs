# Introduction

This lab demonstrates a multi-label document classification problem using scikit-learn. The dataset is generated randomly based on the following process:

- Pick the number of labels: n ~ Poisson(n_labels)
- N times, choose a class c: c ~ Multinomial(theta)
- Pick the document length: k ~ Poisson(length)
- K times, choose a word: w ~ Multinomial(theta_c)

In this process, rejection sampling is used to ensure that n is more than 2, and that the document length is never zero. Likewise, classes that have already been chosen are rejected. The documents that are assigned to both classes are plotted surrounded by two colored circles.

> You can open the `plot-multilabel.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
