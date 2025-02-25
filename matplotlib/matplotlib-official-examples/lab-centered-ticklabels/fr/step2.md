# Créer le graphique

Ensuite, nous allons créer le graphique à l'aide de la fonction `subplots()` de Matplotlib et tracer le prix de clôture ajusté des actions de Google en fonction du temps.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```
