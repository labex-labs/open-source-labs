# Calcular os Coeficientes de uma Regressão Bayesiana com GridSearch

```python
cv = KFold(2)  # gerador de validação cruzada para seleção de modelo
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```
