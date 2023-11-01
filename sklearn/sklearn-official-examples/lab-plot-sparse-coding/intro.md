# Introduction

In this lab, we will learn how to transform a signal as a sparse combination of Ricker wavelets using sparse coding methods. The Ricker (also known as Mexican hat or the second derivative of a Gaussian) is not a particularly good kernel to represent piecewise constant signals like this one. It can therefore be seen how much adding different widths of atoms matters and it therefore motivates learning the dictionary to best fit your type of signals.

We will visually compare different sparse coding methods using the `SparseCoder` estimator. The richer dictionary on the right is not larger in size, heavier subsampling is performed in order to stay on the same order of magnitude.

> You can open the `plot-sparse-coding.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

