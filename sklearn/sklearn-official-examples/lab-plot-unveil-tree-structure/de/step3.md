# Visualisiere den Entscheidungsbaum

Wir können den Entscheidungsbaum auch mit der `plot_tree`-Funktion aus dem `tree`-Modul von scikit-learn visualisieren.

```python
from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(clf)
plt.show()
```
