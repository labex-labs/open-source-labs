# Import Matplotlib

Avant de pouvoir commencer à annoter des graphiques avec Matplotlib, nous devons tout d'abord importer la bibliothèque. Dans cette étape, nous allons importer Matplotlib et créer un graphique simple pour l'annotation.

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```
