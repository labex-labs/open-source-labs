# 绘制有噪声重构结果

```python
omp.fit(X, y_noisy)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 3)
plt.xlim(0, 512)
plt.title("从有噪声测量中恢复的信号")
plt.stem(idx_r, coef[idx_r])
```
