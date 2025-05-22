# Introduction

In this lab, we will learn how to estimate and visualize the variance of the Receiver Operating Characteristic (ROC) metric using cross-validation in Python. ROC curves are used in binary classification to measure the performance of a model by plotting the true positive rate (TPR) against the false positive rate (FPR). We will use the Scikit-learn library to load the iris dataset, create noisy features, and classify the dataset with Support Vector Machine (SVM). We will then plot the ROC curves with cross-validation and calculate the mean Area Under the Curve (AUC) to see the variability of the classifier output when the training set is split into different subsets.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
