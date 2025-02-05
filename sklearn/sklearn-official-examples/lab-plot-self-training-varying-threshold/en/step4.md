# Define Threshold Values

```python
x_values = np.arange(0.4, 1.05, 0.05)
x_values = np.append(x_values, 0.99999)
```

We define an array of threshold values ranging from 0.4 to 1, with steps of 0.05. We then append a very high threshold value of 0.99999 to ensure that we include a threshold value that will not result in any self-labeled samples.
