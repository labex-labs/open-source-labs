# Introduction

This lab demonstrates how to use KBinsDiscretizer from the Scikit-learn library to perform vector quantization on a sample image of a raccoon face. Vector quantization is a technique to reduce the number of gray levels used to represent an image. We will use KBinsDiscretizer to perform vector quantization on the raccoon face image. We will use 8 gray levels to represent the image, which can be compressed to use only 3 bits per pixel. We will compare the uniform and k-means clustering strategies to map the pixel values to the 8 gray levels.

> You can write code in `plot-face-compress.ipynb`.
