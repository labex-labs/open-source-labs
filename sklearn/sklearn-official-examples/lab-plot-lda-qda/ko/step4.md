# LDA 공분산 타원 플롯

LDA 의 공분산 타원체를 플롯합니다.

```python
def plot_lda_cov(lda, splot):
    plot_ellipse(splot, lda.means_[0], lda.covariance_, "red")
    plot_ellipse(splot, lda.means_[1], lda.covariance_, "blue")
```
