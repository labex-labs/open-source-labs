# Graficar la reconstrucción con ruido con el número de ceros no nulos establecido por CV

```python
omp_cv = OrthogonalMatchingPursuitCV()
omp_cv.fit(X, y_noisy)
coef = omp_cv.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 4)
plt.xlim(0, 512)
plt.title("Señal recuperada a partir de mediciones con ruido con CV")
plt.stem(idx_r, coef[idx_r])

plt.subplots_adjust(0.06, 0.04, 0.94, 0.90, 0.20, 0.38)
plt.suptitle("Recuperación de señal esparsa con Orthogonal Matching Pursuit", fontsize=16)
plt.show()
```
