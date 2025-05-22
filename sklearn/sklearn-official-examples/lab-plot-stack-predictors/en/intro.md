# Introduction

In this lab, we will be using the Stacking method to blend several estimators to make predictions. In this strategy, some estimators are individually fitted on some training data while a final estimator is trained using the stacked predictions of these base estimators. We will be using the Ames Housing dataset to predict the final logarithmic price of the houses. We will use 3 learners, linear and non-linear and use a ridge regressor to combine their outputs together. We will also compare the performance of each individual predictor as well as of the stack of the regressors.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
