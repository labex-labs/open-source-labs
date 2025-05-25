# Gerar Dados Esparsos

Em seguida, geramos alguns dados esparsos que usaremos para a regressão Lasso. Copiamos os dados densos da etapa anterior e substituímos todos os valores menores que 2,5 por 0. Também convertemos os dados esparsos para o formato Compressed Sparse Column do Scipy.

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
