# 绘制线性判别分析（LDA）的协方差椭圆

我们将绘制线性判别分析（LDA）的协方差椭球体。

```python
def plot_lda_cov(lda, splot):
    plot_ellipse(splot, lda.means_[0], lda.covariance_, "red")
    plot_ellipse(splot, lda.means_[1], lda.covariance_, "blue")
```
