# Skewed Chi Squared (SCS) Kernel Approximation

The SCS kernel is a variant of the exponentiated chi squared kernel that allows for a simple Monte Carlo approximation of the feature map. The SkewedChi2Sampler class provides an approximate mapping for this kernel.

To use SkewedChi2Sampler for kernel approximation, follow these steps:

1. Initialize the SkewedChi2Sampler object with the desired number of samples (n) and the regularization parameter (c).

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. Fit the SkewedChi2Sampler object to your training data.

```python
skewed_chi2_sampler.fit(X_train)
```

3. Transform your training and test data using the SkewedChi2Sampler object.

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```
