# Determinar o Melhor Valor de Alpha

Queremos determinar o melhor valor de alpha a utilizar para podar a árvore de decisão. Podemos fazer isso plotando a precisão versus alpha para os conjuntos de treino e teste.

```python
train_scores = [clf.score(X_train, y_train) for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots()
ax.set_xlabel("alpha")
ax.set_ylabel("precisão")
ax.set_title("Precisão vs alpha para os conjuntos de treino e teste")
ax.plot(ccp_alphas, train_scores, marker="o", label="treino", drawstyle="steps-post")
ax.plot(ccp_alphas, test_scores, marker="o", label="teste", drawstyle="steps-post")
ax.legend()
plt.show()
```
