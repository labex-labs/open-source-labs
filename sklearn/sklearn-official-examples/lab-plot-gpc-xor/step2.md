# Creating XOR Dataset

In this step, we will create an XOR dataset using numpy. We will use logical_xor function to create labels based on the input features.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
