# Tracer la reconstruction bruyante

```python
omp.fit(X, y_noisy)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 3)
plt.xlim(0, 512)
plt.title("Signal reconstitué à partir de mesures bruyantes")
plt.stem(idx_r, coef[idx_r])
```
