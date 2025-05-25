# Determinar os Valores Adequados de Alpha

Queremos determinar os valores apropriados de alpha a utilizar para podar a árvore de decisão. Podemos fazer isto representando a impureza total das folhas versus os alphas efectivos da árvore podada.

```python
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

clf = DecisionTreeClassifier(random_state=0)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

fig, ax = plt.subplots()
ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax.set_xlabel("alpha efectivo")
ax.set_ylabel("impureza total das folhas")
ax.set_title("Impureza Total vs alpha efectivo para o conjunto de treino")
```
