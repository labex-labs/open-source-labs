# Introduction

This lab demonstrates how to use quantile regression to create prediction intervals using scikit-learn. We will generate synthetic data for a regression problem, apply the function to it, and create observations of the target using a lognormal distribution. We will then split the data into training and test datasets, fit non-linear quantile and least squares regressors, and create an evenly spaced evaluation set of input values spanning the [0, 10] range. We will compare the predicted median with the predicted mean, analyze the error metrics, and calibrate the confidence interval. Finally, we will tune the hyper-parameters of the quantile regressors.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
