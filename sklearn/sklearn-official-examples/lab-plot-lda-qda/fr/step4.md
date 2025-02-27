# Tracer les ellipsoïdes de covariance de l'Analyse Discriminante Linéaire (LDA)

Nous allons tracer les ellipsoïdes de covariance pour l'Analyse Discriminante Linéaire (LDA).

```python
def plot_lda_cov(lda, splot):
    plot_ellipse(splot, lda.means_[0], lda.covariance_, "red")
    plot_ellipse(splot, lda.means_[1], lda.covariance_, "blue")
```
