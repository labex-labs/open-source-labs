# Introduction

In this lab, we will explore how boosting can improve prediction accuracy on a multi-class problem. We will use a dataset constructed by taking a ten-dimensional standard normal distribution and defining three classes separated by nested concentric ten-dimensional spheres such that roughly equal numbers of samples are in each class.

We will compare the performance of the SAMME and SAMME.R algorithms. SAMME.R uses the probability estimates to update the additive model, while SAMME uses the classifications only.

> You can open the `plot-adaboost-multiclass.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

