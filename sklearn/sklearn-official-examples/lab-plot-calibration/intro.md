# Introduction

In classification tasks, it is often important to predict not only the class label but also the associated probability. The probability indicates the confidence of the prediction. However, not all classifiers provide well-calibrated probabilities, some being over-confident while others being under-confident. A separate calibration of predicted probabilities is often desirable as a postprocessing. This lab illustrates two different methods for this calibration and evaluates the quality of the returned probabilities using Brier's score.

> You can open the `plot-calibration.ipynb` in WebIDE to start the exercises. Learn how to use [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
> ![](https://file.labex.io/upload/u/1991/fzLMg1oHuQrI.png)
> We can not verify your answers automatically in this lab.
