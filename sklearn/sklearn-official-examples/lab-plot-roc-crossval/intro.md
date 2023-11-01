# Introduction

In this lab, we will learn how to estimate and visualize the variance of the Receiver Operating Characteristic (ROC) metric using cross-validation in Python. ROC curves are used in binary classification to measure the performance of a model by plotting the true positive rate (TPR) against the false positive rate (FPR). We will use the Scikit-learn library to load the iris dataset, create noisy features, and classify the dataset with Support Vector Machine (SVM). We will then plot the ROC curves with cross-validation and calculate the mean Area Under the Curve (AUC) to see the variability of the classifier output when the training set is split into different subsets.

> You can open the `plot-roc-crossval.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
