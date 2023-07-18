# Summary

This lab demonstrated how to precompute the gram matrix while using weighted samples with an ElasticNet. We first loaded a regression dataset and created a lognormal weight vector which was normalized to sum to the total number of samples. We then centered the design matrix, rescaled it by the normalized weights, and computed the gram matrix. Finally, we fit the elastic net using the precomputed gram matrix and the normalized weights.
