# Introduction

This lab demonstrates how to use KBinsDiscretizer from the Scikit-learn library to perform vector quantization on a sample image of a raccoon face. Vector quantization is a technique to reduce the number of gray levels used to represent an image. We will use KBinsDiscretizer to perform vector quantization on the raccoon face image. We will use 8 gray levels to represent the image, which can be compressed to use only 3 bits per pixel. We will compare the uniform and k-means clustering strategies to map the pixel values to the 8 gray levels.

> You can open the `plot-face-compress.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
