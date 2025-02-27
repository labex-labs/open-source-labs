# Tracer les résultats

Enfin, nous pouvons tracer les résultats pour visualiser les performances du modèle pour différents nombres d'itérations. Nous allons tracer la perte logarithmique négative sur l'axe des y et le nombre d'itérations sur l'axe des x.

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('Nombre d\'itérations')
plt.ylabel('Perte logarithmique négative')
plt.legend()
plt.show()
```
