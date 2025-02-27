# Zeichnen der rekonstruierten rauschenden Signale

```python
omp.fit(X, y_noisy)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 3)
plt.xlim(0, 512)
plt.title("Rekonstruiertes Signal aus rauschenden Messungen")
plt.stem(idx_r, coef[idx_r])
```
