# Introduction

In this lab, we will demonstrate how to robustly fit a linear model to faulty data using the RANSAC algorithm in scikit-learn. The ordinary linear regressor is sensitive to outliers, and the fitted line can easily be skewed away from the true underlying relationship of data. The RANSAC regressor automatically splits the data into inliers and outliers, and the fitted line is determined only by the identified inliers. We will use the make_regression dataset from scikit-learn to generate random data with outliers, and then fit both a linear model and a RANSAC regressor to the data.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
