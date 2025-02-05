# Introduction

This tutorial demonstrates how to generate high-resolution tricontouring plots with Matplotlib. Tricontouring is a technique used to represent data on an unstructured triangular mesh. It is often used when data is collected at irregularly spaced points, or when the data is inherently triangular in nature. The tutorial will show how to generate a random set of points, perform a Delaunay triangulation on those points, mask out some of the triangles in the mesh, refine and interpolate the data, and finally plot the refined data using Matplotlib's `tricontour` function.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
