# ノイジーな再構成をプロットする

```python
omp.fit(X, y_noisy)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 3)
plt.xlim(0, 512)
plt.title("ノイジーな測定値から回復した信号")
plt.stem(idx_r, coef[idx_r])
```
