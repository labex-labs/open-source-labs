# Criar e ajustar uma árvore de decisão AdaBoost

Neste passo, criaremos uma árvore de decisão AdaBoost utilizando a classe `AdaBoostClassifier` do módulo `sklearn.ensemble`. Usaremos a árvore de decisão como estimador base e definiremos o parâmetro `max_depth` para 1. Também definiremos o parâmetro `algorithm` para "SAMME" e o parâmetro `n_estimators` para 200. Finalmente, ajustaremos o classificador ao conjunto de dados.

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
