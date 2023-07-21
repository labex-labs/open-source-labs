# Generate Data

In this step, we will generate the data for training and testing the SVM classifier. We will generate 300 random data points with two features. The target to predict is an XOR of the inputs.

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
