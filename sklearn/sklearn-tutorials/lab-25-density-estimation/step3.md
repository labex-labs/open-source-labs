# Fit a kernel density estimator

Now, we will create an instance of the `KernelDensity` estimator and fit it to our data. We can choose the type of kernel and bandwidth for the estimator. For example, we can use a Gaussian kernel and set the bandwidth to 0.2.

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
