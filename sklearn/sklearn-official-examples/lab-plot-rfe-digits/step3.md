# Rank the Features

After fitting the data to the RFE object, we can rank the features based on their importance. We will use the `ranking_` attribute of the RFE object to get the feature rankings. We will also reshape the rankings to match the shape of the original images.

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```


