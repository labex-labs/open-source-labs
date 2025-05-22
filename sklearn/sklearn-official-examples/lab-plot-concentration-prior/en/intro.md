# Introduction

This lab demonstrates how to use the scikit-learn `BayesianGaussianMixture` class to fit a toy dataset containing a mixture of three Gaussians. The class can adapt its number of mixture components automatically using a concentration prior, which is specified using the `weight_concentration_prior_type` parameter. This lab shows the difference between using a Dirichlet distribution prior and a Dirichlet process prior to select the number of components with non-zero weights.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
