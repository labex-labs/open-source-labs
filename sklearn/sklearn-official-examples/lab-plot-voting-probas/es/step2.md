# Inicializar el VotingClassifier

Luego inicializaremos un VotingClassifier de voto suave con pesos `[1, 1, 5]`, lo que significa que las probabilidades predichas de RandomForestClassifier cuentan 5 veces más que los pesos de los otros clasificadores cuando se calcula la probabilidad promediada.

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```
