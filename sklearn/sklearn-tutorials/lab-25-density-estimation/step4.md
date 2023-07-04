# Score the samples

After fitting the estimator, we can use the `score_samples` method to compute the log-likelihood of the samples under the estimated density function. This will give us a measure of how likely each sample is according to the density estimate.

```python
scores = kde.score_samples(X)
```
