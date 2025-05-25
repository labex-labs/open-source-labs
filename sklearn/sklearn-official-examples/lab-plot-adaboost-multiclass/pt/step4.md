# Criar e Treinar os Modelos

Criaremos dois modelos AdaBoost, um usando SAMME e outro usando SAMME.R. Ambos os modelos utilizarão DecisionTreeClassifier com uma profundidade máxima de 2 e 300 estimadores.

```python
bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2), n_estimators=300, learning_rate=1
)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=300,
    learning_rate=1.5,
    algorithm="SAMME",
)

bdt_real.fit(X_train, y_train)
bdt_discrete.fit(X_train, y_train)
```
