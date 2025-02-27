# Initialisiere den VotingClassifier

Wir werden dann einen Soft-Voting-VotingClassifier mit den Gewichten `[1, 1, 5]` initialisieren, was bedeutet, dass die vorhergesagten Wahrscheinlichkeiten des RandomForestClassifier fünfmal so stark gewichtet werden wie die Wahrscheinlichkeiten der anderen Klassifizierer, wenn die durchschnittliche Wahrscheinlichkeit berechnet wird.

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```
