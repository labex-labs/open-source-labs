# Bestimmen der geeigneten Alpha-Werte

Wir möchten die geeigneten Alpha-Werte bestimmen, die für das Pruning des Entscheidungsbaums verwendet werden sollen. Wir können dies tun, indem wir die Gesamtunreinheit der Blätter gegen die effektiven Alphas des geprunten Baums aufzeichnen.

```python
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

clf = DecisionTreeClassifier(random_state=0)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

fig, ax = plt.subplots()
ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax.set_xlabel("effektive Alpha")
ax.set_ylabel("Gesamtunreinheit der Blätter")
ax.set_title("Gesamtunreinheit gegen effektive Alpha für den Trainingssatz")
```
