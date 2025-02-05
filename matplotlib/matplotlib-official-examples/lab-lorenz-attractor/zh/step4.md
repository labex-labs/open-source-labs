# 计算洛伦兹吸引子

我们通过逐步推进时间，并使用前一个点和洛伦兹函数来估计下一个点，从而计算洛伦兹吸引子。

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```
