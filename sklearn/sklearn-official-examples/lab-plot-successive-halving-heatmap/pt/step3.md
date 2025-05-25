# Executar Halving Sucessivo

Agora, realizaremos a busca de parâmetros usando Halving Sucessivo no mesmo modelo SVC e conjunto de dados usados na Etapa 2.

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
