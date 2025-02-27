# Initialiser le VotingClassifier

Nous allons ensuite initialiser un VotingClassifier à vote mol avec des poids `[1, 1, 5]`, ce qui signifie que les probabilités prédites du RandomForestClassifier comptent 5 fois plus que les poids des autres classifieurs lors du calcul de la probabilité moyenne.

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```
