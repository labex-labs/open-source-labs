# Summary

Lasso is known to recover sparse data effectively but does not perform well with highly correlated features. Indeed, if several correlated features contribute to the target, Lasso would end up selecting a single one of them. In the case of sparse yet non-correlated features, a Lasso model would be more suitable.

ElasticNet introduces some sparsity on the coefficients and shrinks their values to zero. Thus, in the presence of correlated features that contribute to the target, the model is still able to reduce their weights without setting them exactly to zero. This results in a less sparse model than a pure Lasso and may capture non-predictive features as well.

ARDRegression is better when handling Gaussian noise, but is still unable to handle correlated features and requires a larger amount of time due to fitting a prior.
