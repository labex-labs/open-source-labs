# Introduction

This tutorial will demonstrate how to perform quantile regression using scikit-learn. We will generate two synthetic datasets to illustrate how quantile regression can predict non-trivial conditional quantiles. We will use the `QuantileRegressor` class to estimate the median as well as a low and high quantile fixed at 5% and 95%, respectively. We will compare `QuantileRegressor` with `LinearRegression` and evaluate their performance using mean absolute error (MAE) and mean squared error (MSE).

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
