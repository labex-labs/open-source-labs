# Introduction

In this lab, you will learn how to use the multiprocessing library and Matplotlib to plot data generated from a separate process. We will create two classes - `ProcessPlotter` and `NBPlot` - to handle the plotting and data generation, respectively. The `NBPlot` class will generate random data and send it to the `ProcessPlotter` class through a pipe, which will then plot the data in real-time.

> You can open the `multiprocess-sgskip.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> Labby cannot automatically verify the answers because it cannot access the notebook.
