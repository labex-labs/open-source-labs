# Créer une figure avec deux sous-graphiques

Tout d'abord, nous devons créer une figure avec deux sous-graphiques. Nous allons utiliser la méthode `plt.subplots()` pour créer une figure avec deux sous-graphiques côte à côte.

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
