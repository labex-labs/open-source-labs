# Création du tracé

Maintenant, nous allons créer le tracé en utilisant `matplotlib.pyplot`. Nous allons tracer l'onde sinusoïdale et ajouter une ligne horizontale à y = 0.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```
