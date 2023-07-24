# Introduction

In classification tasks, it is often important to predict not only the class label but also the associated probability. The probability indicates the confidence of the prediction. However, not all classifiers provide well-calibrated probabilities, some being over-confident while others being under-confident. A separate calibration of predicted probabilities is often desirable as a postprocessing. This lab illustrates two different methods for this calibration and evaluates the quality of the returned probabilities using Brier's score.

> You can write code in `plot-calibration.ipynb`.
