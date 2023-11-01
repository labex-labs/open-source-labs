# Introduction

This lab demonstrates how to use the scikit-learn API to process a large dataset of faces and learn a set of 20 x 20 image patches that represent faces. The key aspect of this lab is the use of online learning, where we load and process images one at a time and extract 50 random patches from each image. We accumulate 500 patches (from 10 images) and then run the online KMeans object, MiniBatchKMeans' partial_fit method.

> You can open the `plot-dict-face-patches.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
