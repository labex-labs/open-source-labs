# Criando um Objeto Halving Random Search

Crie um objeto `HalvingRandomSearchCV` para pesquisar no espaço de parâmetros. O objeto recebe os seguintes argumentos:

- `estimator`: o estimador a ser otimizado
- `param_distributions`: o espaço de parâmetros a ser pesquisado
- `factor`: o fator pelo qual o número de candidatos é reduzido em cada iteração
- `random_state`: o estado aleatório usado para a pesquisa

O código para criar o objeto é o seguinte:

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
