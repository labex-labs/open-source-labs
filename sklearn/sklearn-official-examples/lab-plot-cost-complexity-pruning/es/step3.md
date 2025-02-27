# Determinar los valores adecuados de alfa

Queremos determinar los valores adecuados de alfa para utilizar en la poda del árbol de decisión. Esto se puede hacer trazando la impureza total de las hojas en función de los alfas efectivos del árbol podado.

```python
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

clf = DecisionTreeClassifier(random_state=0)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

fig, ax = plt.subplots()
ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax.set_xlabel("alpha efectivo")
ax.set_ylabel("impureza total de las hojas")
ax.set_title("Impureza total vs alpha efectivo para el conjunto de entrenamiento")
```
