# Create the Data

We will now create some random data that will contain outliers. We will use `numpy.random.rand` to generate 30 random numbers and then add two outliers to the data.

```python
np.random.seed(19680801)

pts = np.random.rand(30)*.2
# Now let's make two outlier points which are far away from everything.
pts[[3, 14]] += .8
```
