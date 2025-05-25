# Executar busca aleatorizada com validação cruzada

A busca aleatorizada amostra aleatoriamente um subconjunto da grade de parâmetros e avalia o desempenho de cada combinação usando validação cruzada. É útil quando o espaço de parâmetros é grande e a busca exaustiva não é viável.

```python
# Criar uma instância de RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Ajustar os dados para executar a busca aleatorizada
random_search.fit(X, y)

# Imprimir a melhor combinação de hiperparâmetros
print('Melhores hiperparâmetros:', random_search.best_params_)
```
