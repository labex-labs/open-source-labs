# Построение графика восстановления с шумом

```python
omp.fit(X, y_noisy)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 3)
plt.xlim(0, 512)
plt.title("Восстановленный сигнал из измерений с шумом")
plt.stem(idx_r, coef[idx_r])
```
