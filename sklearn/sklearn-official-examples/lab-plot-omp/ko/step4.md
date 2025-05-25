# 노이즈가 없는 재구성 시각화

```python
omp = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs)
omp.fit(X, y)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 2)
plt.xlim(0, 512)
plt.title("노이즈가 없는 측정값으로부터 복원된 신호")
plt.stem(idx_r, coef[idx_r])
```
