# Treinar e avaliar os classificadores

Treinaremos cada classificador em diferentes proporções dos dados de treino, variando de 1% a 95%, e avaliaremos seu desempenho no conjunto de teste. Repetimos este processo 10 vezes para obter uma estimativa mais precisa da taxa de erro de teste.

```python
heldout = [0.01, 0.05, 0.25, 0.5, 0.75, 0.9, 0.95]
rounds = 10
xx = 1.0 - np.array(heldout)

for name, clf in classifiers:
    print("Treinando %s" % name)
    yy = []
    for i in heldout:
        yy_ = []
        for r in range(rounds):
            X_train_, X_test_, y_train_, y_test_ = train_test_split(X_train, y_train, test_size=i, random_state=r)
            clf.fit(X_train_, y_train_)
            y_pred = clf.predict(X_test_)
            yy_.append(1 - np.mean(y_pred == y_test_))
        yy.append(np.mean(yy_))
    plt.plot(xx, yy, label=name)

plt.legend(loc="upper right")
plt.xlabel("Proporção dos dados de treino")
plt.ylabel("Taxa de erro de teste")
plt.show()
```
