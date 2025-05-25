# Criar um objeto GridSearchCV e ajustar os dados

Criaremos um objeto `GridSearchCV` usando o pipeline e a grade de parâmetros definidos na etapa anterior. Em seguida, ajustaremos os dados ao objeto.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```
