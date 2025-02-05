# Introduction

Principal Component Regression (PCR) and Partial Least Squares Regression (PLS) are two methods used in regression analysis. PCR involves applying PCA to training data, followed by training a regressor on the transformed samples. The PCA transformation is unsupervised, meaning that no information about the targets is used. As a result, PCR may perform poorly in some datasets where the target is strongly correlated with directions that have low variance.

PLS is both a transformer and a regressor, and it is quite similar to PCR. It also applies a dimensionality reduction to the samples before applying a linear regressor to the transformed data. The main difference with PCR is that the PLS transformation is supervised. Therefore, it does not suffer from the issue mentioned above.

In this lab, we will compare PCR and PLS on a toy dataset.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
