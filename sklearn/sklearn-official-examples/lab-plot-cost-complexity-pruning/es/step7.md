# Determinar el mejor valor de alfa

Queremos determinar el mejor valor de alfa para utilizar en la poda del árbol de decisión. Esto se puede hacer trazando la precisión en función del alfa para los conjuntos de entrenamiento y prueba.

```python
train_scores = [clf.score(X_train, y_train) for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots()
ax.set_xlabel("alpha")
ax.set_ylabel("precisión")
ax.set_title("Precisión vs alpha para los conjuntos de entrenamiento y prueba")
ax.plot(ccp_alphas, train_scores, marker="o", label="entrenamiento", drawstyle="steps-post")
ax.plot(ccp_alphas, test_scores, marker="o", label="prueba", drawstyle="steps-post")
ax.legend()
plt.show()
```
