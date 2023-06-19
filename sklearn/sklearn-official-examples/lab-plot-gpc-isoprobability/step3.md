# Train the Model

We will use a GPC model to classify the data. First, we need to specify the kernel function.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

Then, we can create a GPC model and train it using the data.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```


