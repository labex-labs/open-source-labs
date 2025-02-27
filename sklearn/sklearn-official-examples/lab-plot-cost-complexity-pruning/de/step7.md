# Bestimmen des besten Alpha-Werts

Wir möchten den besten Alpha-Wert bestimmen, der für das Pruning des Entscheidungsbaums verwendet werden soll. Wir können dies tun, indem wir die Genauigkeit gegen Alpha für die Trainings- und Testsets aufzeichnen.

```python
train_scores = [clf.score(X_train, y_train) for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots()
ax.set_xlabel("alpha")
ax.set_ylabel("Genauigkeit")
ax.set_title("Genauigkeit gegen alpha für Trainings- und Testsets")
ax.plot(ccp_alphas, train_scores, marker="o", label="train", drawstyle="steps-post")
ax.plot(ccp_alphas, test_scores, marker="o", label="test", drawstyle="steps-post")
ax.legend()
plt.show()
```
