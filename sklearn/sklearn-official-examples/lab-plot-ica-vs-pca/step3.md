# Use FastICA Algorithm

In this step, we use FastICA algorithm, which finds directions in the feature space corresponding to projections with high non-Gaussianity.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Estimate the sources

S_ica_ /= S_ica_.std(axis=0)
```


