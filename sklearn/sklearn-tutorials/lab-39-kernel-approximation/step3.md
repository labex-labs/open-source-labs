# Additive Chi Squared (ACS) Kernel Approximation

The ACS kernel is a kernel on histograms, commonly used in computer vision. The AdditiveChi2Sampler class provides an approximate mapping for this kernel.

To use AdditiveChi2Sampler for kernel approximation, follow these steps:

1. Initialize the AdditiveChi2Sampler object with the desired number of samples (n) and the regularization parameter (c).

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. Fit the AdditiveChi2Sampler object to your training data.

```python
additive_chi2_sampler.fit(X_train)
```

3. Transform your training and test data using the AdditiveChi2Sampler object.

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
