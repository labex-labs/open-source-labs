# Introduction

Novelty and outlier detection are techniques used to identify whether a new observation belongs to the same distribution as existing observations or if it should be considered as different. These techniques are commonly used to clean real datasets by identifying abnormal or unusual observations.

There are two important distinctions in this context:

1. Outlier detection: The training data contains outliers, which are observations that are far from the others. Outlier detection estimators try to fit the regions where the training data is the most concentrated, ignoring the deviant observations.
2. Novelty detection: The training data is not polluted by outliers, and the goal is to detect whether a new observation is an outlier. In this context, an outlier is also called a novelty.

The scikit-learn project provides a set of machine learning tools that can be used for both novelty and outlier detection. These tools are implemented using unsupervised learning algorithms, which means they learn patterns from the data without the need for labeled examples.

> You can open the `24-novelty-and-outlier-detection.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> Labby cannot automatically verify the answers because it cannot access the notebook.
