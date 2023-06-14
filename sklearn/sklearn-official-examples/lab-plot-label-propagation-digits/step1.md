# Load and Shuffle Data

We first load the digits dataset and randomly shuffle the data.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```


