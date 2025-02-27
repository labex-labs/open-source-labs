# Déterminer les valeurs appropriées d'alpha

Nous voulons déterminer les valeurs appropriées d'alpha à utiliser pour tailler l'arbre de décision. Nous pouvons le faire en traçant l'impureté totale des feuilles en fonction des alphas effectifs de l'arbre taillé.

```python
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

clf = DecisionTreeClassifier(random_state=0)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

fig, ax = plt.subplots()
ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax.set_xlabel("alpha effectif")
ax.set_ylabel("impureté totale des feuilles")
ax.set_title("Impureté totale vs alpha effectif pour l'ensemble d'entraînement")
```
