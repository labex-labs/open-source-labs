# Zeichnen der rekonstruierten rauchfreien Signale

```python
omp = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs)
omp.fit(X, y)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 2)
plt.xlim(0, 512)
plt.title("Rekonstruiertes Signal aus rauchfreien Messungen")
plt.stem(idx_r, coef[idx_r])
```
