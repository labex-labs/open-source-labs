# Introduction

This tutorial demonstrates how to generate high-resolution tricontouring plots with Matplotlib. Tricontouring is a technique used to represent data on an unstructured triangular mesh. It is often used when data is collected at irregularly spaced points, or when the data is inherently triangular in nature. The tutorial will show how to generate a random set of points, perform a Delaunay triangulation on those points, mask out some of the triangles in the mesh, refine and interpolate the data, and finally plot the refined data using Matplotlib's `tricontour` function.

> You can open the `tricontour-smooth-delaunay.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.

