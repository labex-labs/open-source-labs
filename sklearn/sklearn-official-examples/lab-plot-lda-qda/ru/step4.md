# Построение эллипсов ковариации для LDA

Мы построим эллипсоиды ковариации для LDA.

```python
def plot_lda_cov(lda, splot):
    plot_ellipse(splot, lda.means_[0], lda.covariance_, "red")
    plot_ellipse(splot, lda.means_[1], lda.covariance_, "blue")
```
