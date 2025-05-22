# Introduction

In machine learning, every estimator has its advantages and drawbacks. The generalization error of an estimator can be decomposed into bias, variance, and noise. The bias of an estimator is the average error for different training sets, while the variance indicates its sensitivity to varying training sets. Noise is a property of the data.

In this lab, we will explore how to use validation curves to evaluate the performance of machine learning models. Validation curves allow us to plot the influence of a single hyperparameter on the training score and the validation score, helping us determine if the model is overfitting or underfitting for different hyperparameter values.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
