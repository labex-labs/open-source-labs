# Introduction

In this lab, we will be using the Ames Housing dataset to compare different methods of handling categorical features in Gradient Boosting estimators. The dataset contains both numerical and categorical features, and the target is the sales price of the houses. We will compare the performance of four different pipelines:

- Dropping the categorical features
- One-hot encoding the categorical features
- Treating the categorical features as ordinal values
- Using native categorical support in the Gradient Boosting estimator

We will evaluate the pipelines in terms of their fit times and prediction performances using cross-validation.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access Jupyter Notebook for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
