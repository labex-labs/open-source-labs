# 노이즈가 있는 재구성 시각화

```python
omp.fit(X, y_noisy)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 3)
plt.xlim(0, 512)
plt.title("노이즈가 있는 측정값으로부터 복원된 신호")
plt.stem(idx_r, coef[idx_r])
```
