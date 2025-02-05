# 绘制通过交叉验证设置非零值数量的有噪声重构结果

```python
omp_cv = OrthogonalMatchingPursuitCV()
omp_cv.fit(X, y_noisy)
coef = omp_cv.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 4)
plt.xlim(0, 512)
plt.title("通过交叉验证从有噪声测量中恢复的信号")
plt.stem(idx_r, coef[idx_r])

plt.subplots_adjust(0.06, 0.04, 0.94, 0.90, 0.20, 0.38)
plt.suptitle("使用正交匹配追踪的稀疏信号恢复", fontsize=16)
plt.show()
```
