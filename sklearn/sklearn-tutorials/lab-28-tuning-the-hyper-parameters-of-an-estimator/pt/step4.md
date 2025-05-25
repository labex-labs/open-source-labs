# Executar busca em grade com validação cruzada

A busca em grade pesquisa exaustivamente todas as combinações possíveis de hiperparâmetros na grade de parâmetros especificada. Avalia o desempenho de cada combinação usando validação cruzada.

```python
# Criar uma instância de GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Ajustar os dados para executar a busca em grade
grid_search.fit(X, y)

# Imprimir a melhor combinação de hiperparâmetros
print('Melhores hiperparâmetros:', grid_search.best_params_)
```
