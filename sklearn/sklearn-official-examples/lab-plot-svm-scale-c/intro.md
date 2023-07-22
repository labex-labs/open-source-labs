# Introduction

This lab demonstrates the effect of scaling the regularization parameter when using Support Vector Machines (SVMs) for classification. In SVM classification, we are interested in a risk minimization for the equation:

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

where:

- `C` is used to set the amount of regularization
- `L` is a loss function of our samples and our model parameters.
- `Ω` is a penalty function of our model parameters

> You can write code in `plot-svm-scale-c.ipynb`.
