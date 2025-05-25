# Executar Busca em Grade

Usaremos a Busca em Grade para realizar a busca de parâmetros no modelo SVC. Usaremos o conjunto de dados sintético gerado e a grade de parâmetros gerada na Etapa 1.

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
