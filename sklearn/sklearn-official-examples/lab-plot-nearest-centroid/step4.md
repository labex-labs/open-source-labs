# Create and Fit the Classifier

We create an instance of Nearest Centroid Classifier with a shrinkage value of 0.2 and fit the data.

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```


