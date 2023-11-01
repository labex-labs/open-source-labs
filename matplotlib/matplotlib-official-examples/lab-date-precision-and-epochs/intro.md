# Introduction

This is a step-by-step lab that demonstrates how to handle date precision and epochs in Matplotlib. Matplotlib can work with `.datetime` objects and `numpy.datetime64` objects using a unit converter that recognizes these dates and converts them to floating point numbers. Before Matplotlib 3.3, the default for this conversion returns a float that was days since "0000-12-31T00:00:00". As of Matplotlib 3.3, the default is days from "1970-01-01T00:00:00". This allows more resolution for modern dates.

> You can open the `date-precision-and-epochs.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

