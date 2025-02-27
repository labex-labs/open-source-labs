# Graficar los resultados

Finalmente, podemos graficar los resultados para visualizar el rendimiento del modelo para diferentes números de iteraciones. Graficaremos la pérdida logarítmica negativa en el eje y y el número de iteraciones en el eje x.

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('Number of iterations')
plt.ylabel('Negative log-loss')
plt.legend()
plt.show()
```
