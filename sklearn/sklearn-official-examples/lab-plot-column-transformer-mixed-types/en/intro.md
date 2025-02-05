# Introduction

This lab illustrates how to apply different preprocessing and feature extraction pipelines to different subsets of features, using `ColumnTransformer`. This is particularly handy for the case of datasets that contain heterogeneous data types, since we may want to scale the numeric features and one-hot encode the categorical ones.

In this lab, we will be using the Titanic dataset from OpenML to build a pipeline that preprocesses both categorical and numeric data using `ColumnTransformer` and use that to train a logistic regression model.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
