# Introduction

This lab demonstrates an example of using classifier chain on a multilabel dataset. The Classifier Chain algorithm is a modification of the problem transformation method for multi-label classification. This method exploits the correlation among the classes by building a chain of binary classifiers. Each model gets the predictions of the preceding models in the chain as features. We will use the `yeast` dataset which contains 2417 datapoints each with 103 features and 14 possible labels. Each data point has at least one label. As a baseline we first train a logistic regression classifier for each of the 14 labels. To evaluate the performance of these classifiers we predict on a held-out test set and calculate the Jaccard score for each sample.

> You can open the `plot-classifier-chain-yeast.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

