# Treinar um classificador usando SGD

Agora, treinaremos um classificador usando a classe SGDClassifier. Usaremos a função de perda log_loss e a penalidade l2.

```python
# Treinar um classificador usando SGD
clf = SGDClassifier(loss="log_loss", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = clf.predict(X_test)

# Medir a precisão do classificador
accuracy = accuracy_score(y_test, y_pred)

# Imprimir a precisão
print("Precisão do Classificador:", accuracy)
```
