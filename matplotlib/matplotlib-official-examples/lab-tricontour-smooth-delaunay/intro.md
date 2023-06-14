# Introduction

This tutorial demonstrates how to generate high-resolution tricontouring plots with Matplotlib. Tricontouring is a technique used to represent data on an unstructured triangular mesh. It is often used when data is collected at irregularly spaced points, or when the data is inherently triangular in nature. The tutorial will show how to generate a random set of points, perform a Delaunay triangulation on those points, mask out some of the triangles in the mesh, refine and interpolate the data, and finally plot the refined data using Matplotlib's `tricontour` function.

#

> You can write code in `tricontour-smooth-delaunay.ipynb`.
