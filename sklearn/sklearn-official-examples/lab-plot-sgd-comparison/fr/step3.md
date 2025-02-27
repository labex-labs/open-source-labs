# Entraîner et évaluer les classifieurs

Nous allons entraîner chaque classifieur avec différentes proportions des données d'entraînement, allant de 1% à 95%, et évaluer leur performance sur l'ensemble de test. Nous allons répéter ce processus 10 fois pour obtenir une estimation plus précise du taux d'erreur sur le test.

```python
heldout = [0.01, 0.05, 0.25, 0.5, 0.75, 0.9, 0.95]
rounds = 10
xx = 1.0 - np.array(heldout)

for name, clf in classifiers:
    print("Training %s" % name)
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
plt.xlabel("Proportion of training data")
plt.ylabel("Test error rate")
plt.show()
```
