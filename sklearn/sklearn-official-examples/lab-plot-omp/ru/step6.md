# Построение графика восстановления с шумом с количеством ненулевых элементов, заданным кросс-валидацией

```python
omp_cv = OrthogonalMatchingPursuitCV()
omp_cv.fit(X, y_noisy)
coef = omp_cv.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 4)
plt.xlim(0, 512)
plt.title("Восстановленный сигнал из измерений с шумом с использованием кросс-валидации")
plt.stem(idx_r, coef[idx_r])

plt.subplots_adjust(0.06, 0.04, 0.94, 0.90, 0.20, 0.38)
plt.suptitle("Восстановление разреженного сигнала с использованием Ортогонального Метода Сопоставления", fontsize=16)
plt.show()
```
