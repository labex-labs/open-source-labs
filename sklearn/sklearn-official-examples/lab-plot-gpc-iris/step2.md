# Defining the kernel function

Next, we will define the kernel function. In this example, we will use the Radial Basis Function (RBF) kernel. We will define two versions of the RBF kernel: an isotropic version and an anisotropic version.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```


