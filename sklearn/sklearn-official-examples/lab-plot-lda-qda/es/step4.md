# Trazar elipses de covarianza del LDA

Traza los elipsoides de covarianza para el LDA.

```python
def plot_lda_cov(lda, splot):
    plot_ellipse(splot, lda.means_[0], lda.covariance_, "red")
    plot_ellipse(splot, lda.means_[1], lda.covariance_, "blue")
```
