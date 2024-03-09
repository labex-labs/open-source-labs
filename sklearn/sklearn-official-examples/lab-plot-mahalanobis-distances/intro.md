# Introduction

In this lab, we will explore the use of robust covariance estimation with Mahalanobis distances on Gaussian distributed data. Mahalanobis distance is a measure of the distance between a point and a distribution. It is defined as the distance between a point and the mean of the distribution, scaled by the inverse of the covariance matrix of the distribution. For Gaussian distributed data, the Mahalanobis distance can be used to compute the distance of an observation to the mode of the distribution. We will compare the performance of the Minimum Covariance Determinant (MCD) estimator, a robust estimator of covariance, with the standard covariance Maximum Likelihood Estimator (MLE) in calculating the Mahalanobis distances of a contaminated dataset.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
