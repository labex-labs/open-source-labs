# 绘制二次判别分析（QDA）的协方差椭圆

我们将绘制二次判别分析（QDA）的协方差椭球体。

```python
def plot_qda_cov(qda, splot):
    plot_ellipse(splot, qda.means_[0], qda.covariance_[0], "red")
    plot_ellipse(splot, qda.means_[1], qda.covariance_[1], "blue")
```
