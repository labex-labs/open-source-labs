# Création du graphique initial

Ensuite, nous créons le graphique initial qui sera mis à jour en fonction de l'entrée de l'utilisateur. Dans cet exemple, nous créons un graphique d'une fonction avec `t` comme variable indépendante.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```
