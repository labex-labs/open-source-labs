# Inicializar o VotingClassifier

Em seguida, inicializaremos um `VotingClassifier` de votação suave com pesos `[1, 1, 5]`. Isso significa que as probabilidades previstas do `RandomForestClassifier` contam 5 vezes mais do que os pesos dos outros classificadores quando a probabilidade média é calculada.

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```
