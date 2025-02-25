# Créer une figure avec quatre sous-graphiques

Nous allons créer une figure avec quatre sous-graphiques pour illustrer les différents aspects de la rastérisation.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
