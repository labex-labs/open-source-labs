# Imprimir Melhores Parâmetros e Pontuação

Imprimiremos os melhores parâmetros e a pontuação obtida do GridSearchCV.

```python
print("Melhor parâmetro (pontuação CV=%0.3f):" % search.best_score_)
print(search.best_params_)
```
