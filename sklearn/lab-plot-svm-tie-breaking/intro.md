# Introduction

This lab introduces SVM tie-breaking and its effect on decision boundary. In SVM, tie-breaking is the mechanism used to resolve the conflicts between the two or more classes when their distances are equal. It is not enabled by default when `decision_function_shape='ovr'` because it is costly. Therefore, this lab illustrates the effect of the `break_ties` parameter for a multiclass classification problem and `decision_function_shape='ovr'`.

> In this lab, You can write code in IPython or in `plot-svm-tie-breaking.py`.
