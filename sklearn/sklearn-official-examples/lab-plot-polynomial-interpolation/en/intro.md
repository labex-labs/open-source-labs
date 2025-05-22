# Introduction

In this lab, we will learn how to approximate a function with polynomials up to a certain degree using ridge regression. We will show two different ways of doing this given `n_samples` of 1d points `x_i`:

1. `PolynomialFeatures`: generates all monomials up to a specified degree. This gives us the Vandermonde matrix with `n_samples` rows and `degree + 1` columns.
2. `SplineTransformer`: generates B-spline basis functions. A basis function of a B-spline is a piece-wise polynomial function of degree `degree` that is non-zero only between `degree+1` consecutive knots.

We will use the `make_pipeline` function to add non-linear features and show how these transformers are well-suited to model non-linear effects with a linear model. We will plot the function, training points, and the interpolation using polynomial features and B-splines. We will also plot all columns of both transformers separately and show the knots of spline. Finally, we will demonstrate the use of periodic splines.

## VM Tips

After the VM startup is done, click the top left corner to switch to the **Notebook** tab to access [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) for practice.

Sometimes, you may need to wait a few seconds for Jupyter Notebook to finish loading. The validation of operations cannot be automated because of limitations in Jupyter Notebook.

If you face issues during learning, feel free to ask Labby. Provide feedback after the session, and we will promptly resolve the problem for you.
