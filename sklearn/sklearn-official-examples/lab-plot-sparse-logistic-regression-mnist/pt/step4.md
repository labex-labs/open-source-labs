# Treinar o Modelo

Treinaremos o modelo usando regressão logística com penalidade L1 e algoritmo SAGA. Definiremos o valor de `C` como 50.0 dividido pelo número de amostras de treino.

```python
# Aumentar a tolerância para uma convergência mais rápida
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
