# Plotar a Reconstrução Livre de Ruído

```python
omp = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs)
omp.fit(X, y)
coef = omp.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 2)
plt.xlim(0, 512)
plt.title("Sinal Recuperado a partir de Medidas Livres de Ruído")
plt.stem(idx_r, coef[idx_r])
```
