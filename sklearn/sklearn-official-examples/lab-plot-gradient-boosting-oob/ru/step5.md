# Построение графиков результатов

Наконец, мы можем построить графики результатов, чтобы визуализировать производительность модели для различных чисел итераций. Мы построим график, где по оси y будет отрицательный логарифмический лосс, а по оси x - число итераций.

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
