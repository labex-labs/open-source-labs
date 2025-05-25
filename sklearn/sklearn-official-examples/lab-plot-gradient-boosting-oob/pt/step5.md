# Plotar os Resultados

Finalmente, podemos plotar os resultados para visualizar o desempenho do modelo para diferentes números de iterações. Plotaremos a perda de log negativo no eixo y e o número de iterações no eixo x.

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('Número de iterações')
plt.ylabel('Perda de log negativo')
plt.legend()
plt.show()
```
