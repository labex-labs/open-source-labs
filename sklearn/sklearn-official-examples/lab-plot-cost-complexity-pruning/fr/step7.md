# Déterminer la meilleure valeur d'alpha

Nous voulons déterminer la meilleure valeur d'alpha à utiliser pour tailler l'arbre de décision. Nous pouvons le faire en traçant la précision en fonction d'alpha pour les ensembles d'entraînement et de test.

```python
train_scores = [clf.score(X_train, y_train) for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots()
ax.set_xlabel("alpha")
ax.set_ylabel("précision")
ax.set_title("Précision vs alpha pour les ensembles d'entraînement et de test")
ax.plot(ccp_alphas, train_scores, marker="o", label="train", drawstyle="steps-post")
ax.plot(ccp_alphas, test_scores, marker="o", label="test", drawstyle="steps-post")
ax.legend()
plt.show()
```
