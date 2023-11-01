# Introduction

This lab demonstrates the effect of scaling the regularization parameter when using Support Vector Machines (SVMs) for classification. In SVM classification, we are interested in a risk minimization for the equation:

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

where:

- `C` is used to set the amount of regularization
- `L` is a loss function of our samples and our model parameters.
- `Ω` is a penalty function of our model parameters

> You can open the `plot-svm-scale-c.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

