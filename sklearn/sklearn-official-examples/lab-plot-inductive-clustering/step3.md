# Generate New Samples

In this step, we will generate new samples and plot them along with the original dataset. We will use the `make_blobs` function again to generate 10 new samples.

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```


