# Train the Model

We will now train the LOF model using the training data. We set the number of neighbors to 20 and novelty to true. We also set the contamination to 0.1.

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```


