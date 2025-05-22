# Introduction

In this lab, we will explore how model complexity influences both prediction accuracy and computational performance. We will be using two datasets - Diabetes Dataset for regression and 20newsgroups Dataset for classification. We will model the complexity influence on three different estimators:

- SGDClassifier (for classification data) which implements stochastic gradient descent learning
- NuSVR (for regression data) which implements Nu support vector regression
- GradientBoostingRegressor builds an additive model in a forward stage-wise fashion

We will vary the model complexity through the choice of relevant model parameters in each of our selected models. Next, we will measure the influence on both computational performance (latency) and predictive power (MSE or Hamming Loss).

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
