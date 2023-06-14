# Prepare Data

We will now prepare the data for kernel density estimation. We will extract the latitude and longitude information from the dataset and convert them to radians.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convert lat/long to radians
```


