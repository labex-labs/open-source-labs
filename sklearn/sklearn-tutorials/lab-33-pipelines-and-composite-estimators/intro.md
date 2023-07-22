# Introduction

In scikit-learn, pipelines and composite estimators are used to combine multiple transformers and estimators into a single model. This is useful when there is a fixed sequence of steps for processing the data, such as feature selection, normalization, and classification. Pipelines can also be used for joint parameter selection and to ensure that statistics from the test data do not leak into the trained model during cross-validation.

> You can write code in `33-pipelines-and-composite-estimators.ipynb`.
