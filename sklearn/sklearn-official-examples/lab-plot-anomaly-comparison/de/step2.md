# Parameter festlegen

Legen Sie die erforderlichen Parameter für das Lab fest.

```python
n_samples = 300
outliers_fraction = 0.15
n_outliers = int(outliers_fraction * n_samples)
n_inliers = n_samples - n_outliers
```
