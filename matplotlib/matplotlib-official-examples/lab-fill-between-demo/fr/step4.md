# Marquage sélectif de régions horizontales sur toute la zone d'un axe

Le même mécanisme de sélection peut être appliqué pour remplir la hauteur verticale totale de l'axe. Pour être indépendant des limites en y, nous ajoutons une transformation qui interprète les valeurs d'abscisses dans les coordonnées des données et les valeurs d'ordonnées dans les coordonnées de l'axe. L'exemple suivant marque les régions dans lesquelles les données en y sont au-dessus d'un seuil donné.

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
