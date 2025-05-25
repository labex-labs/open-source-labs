# Plotar a Reconstrução com Ruído com Número de Não-Zeros Definido por Validação Cruzada

```python
omp_cv = OrthogonalMatchingPursuitCV()
omp_cv.fit(X, y_noisy)
coef = omp_cv.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 4)
plt.xlim(0, 512)
plt.title("Sinal Recuperado a partir de Medidas com Ruído com Validação Cruzada")
plt.stem(idx_r, coef[idx_r])

plt.subplots_adjust(0.06, 0.04, 0.94, 0.90, 0.20, 0.38)
plt.suptitle("Recuperação de Sinal Esparso com Perseguição Ortogonal de Correspondência", fontsize=16)
plt.show()
```
