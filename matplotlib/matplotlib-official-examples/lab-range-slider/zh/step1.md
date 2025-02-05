# 生成一张虚拟图像

首先，我们将使用NumPy的随机模块生成一张虚拟灰度图像。我们将设置种子以确保结果可重现。

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
