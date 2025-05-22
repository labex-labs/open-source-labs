# Introduction

This lab demonstrates the effect of scaling the regularization parameter when using Support Vector Machines (SVMs) for classification. In SVM classification, we are interested in a risk minimization for the equation:

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

where:

- `C` is used to set the amount of regularization
- `L` is a loss function of our samples and our model parameters.
- `Ω` is a penalty function of our model parameters

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
