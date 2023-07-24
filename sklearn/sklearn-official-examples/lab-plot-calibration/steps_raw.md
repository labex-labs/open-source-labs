# Probability Calibration of Classifiers

## Introduction

In classification tasks, it is often important to predict not only the class label but also the associated probability. The probability indicates the confidence of the prediction. However, not all classifiers provide well-calibrated probabilities, some being over-confident while others being under-confident. A separate calibration of predicted probabilities is often desirable as a postprocessing. This lab illustrates two different methods for this calibration and evaluates the quality of the returned probabilities using Brier's score.

## Steps

### Step 1: Generate Synthetic Dataset

First, we generate a synthetic dataset containing three blobs with two classes, where the second blob contains half positive samples and half negative samples. Probability in this blob is therefore 0.5.

### Step 2: Gaussian Naive-Bayes

We use Gaussian Naive-Bayes for classification, which often has poorly calibrated probabilities. We compare the estimated probability using a Gaussian naive Bayes classifier without calibration, with a sigmoid calibration, and with a non-parametric isotonic calibration.

### Step 3: Plot Data and the Predicted Probabilities

We plot the data and the predicted probabilities.

## Summary

In this lab, we generated a synthetic dataset, used Gaussian Naive-Bayes for classification, and compared the estimated probability using a Gaussian naive Bayes classifier without calibration, with a sigmoid calibration, and with a non-parametric isotonic calibration. We then plotted the data and the predicted probabilities. By comparing the Brier score losses, we found that only the non-parametric model is able to provide a probability calibration that returns probabilities close to the expected 0.5 for most of the samples belonging to the middle cluster with heterogeneous labels. This results in a significantly improved Brier score.
