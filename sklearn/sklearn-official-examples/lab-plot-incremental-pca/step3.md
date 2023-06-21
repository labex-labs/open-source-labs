# Perform IPCA

We will perform IPCA on the Iris dataset by initializing an instance of the IPCA class and fitting it to the data.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
