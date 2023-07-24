# Introduction

In this lab, you will learn how to use the multiprocessing library and Matplotlib to plot data generated from a separate process. We will create two classes - `ProcessPlotter` and `NBPlot` - to handle the plotting and data generation, respectively. The `NBPlot` class will generate random data and send it to the `ProcessPlotter` class through a pipe, which will then plot the data in real-time.

> You can write code in `multiprocess-sgskip.ipynb`.
