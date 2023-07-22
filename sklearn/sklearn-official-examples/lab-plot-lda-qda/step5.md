# Plot QDA Covariance Ellipses

We will plot the covariance ellipsoids for QDA.

```python
def plot_qda_cov(qda, splot):
    plot_ellipse(splot, qda.means_[0], qda.covariance_[0], "red")
    plot_ellipse(splot, qda.means_[1], qda.covariance_[1], "blue")
```
