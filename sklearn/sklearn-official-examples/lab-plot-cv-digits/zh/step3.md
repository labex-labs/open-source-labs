# 定义要测试的超参数值

我们将测试正则化参数C的不同值，该参数控制着在最大化间隔和最小化分类误差之间的权衡。我们将测试10个在10^-10和1之间按对数间隔分布的值。

```python
C_s = np.logspace(-10, 0, 10)
```
