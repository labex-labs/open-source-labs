# Introduction

This tutorial will guide you on how to draw a curve with an error band using Python Matplotlib. An error band is used to indicate the uncertainty of the curve. In this example, we assume that the error can be given as a scalar _err_ that describes the uncertainty perpendicular to the curve in every point. We visualize this error as a colored band around the path using a `.PathPatch`. The patch is created from two path segments _(xp, yp)_, and _(xn, yn)_ that are shifted by +/- _err_ perpendicular to the curve _(x, y)_.

> You can open the `curve-error-band.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

