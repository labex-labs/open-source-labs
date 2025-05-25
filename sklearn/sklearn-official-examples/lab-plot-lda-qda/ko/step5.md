# QDA 공분산 타원 플롯

QDA 의 공분산 타원체를 플롯합니다.

```python
def plot_qda_cov(qda, splot):
    plot_ellipse(splot, qda.means_[0], qda.covariance_[0], "red")
    plot_ellipse(splot, qda.means_[1], qda.covariance_[1], "blue")
```
