# Plotar a Reconstrução com Ruído

```python
omp.fit(X, y_noisy)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 3)
plt.xlim(0, 512)
plt.title("Sinal Recuperado a partir de Medidas com Ruído")
plt.stem(idx_r, coef[idx_r])
```
