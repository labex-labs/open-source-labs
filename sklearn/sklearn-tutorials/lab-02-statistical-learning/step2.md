# Reshaping Data

Sometimes the data may not be initially in the shape required by scikit-learn. In such cases, we need to preprocess the data to transform it into the `(n_samples, n_features)` shape. An example of reshaping data is the digits dataset, which consists of 1797 8x8 images of hand-written digits:

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

Output:

```
(1797, 8, 8)
```

To use this dataset with scikit-learn, we need to reshape each 8x8 image into a feature vector of length 64:

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```
