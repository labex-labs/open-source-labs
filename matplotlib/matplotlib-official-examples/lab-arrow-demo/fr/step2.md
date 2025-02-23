# Définition des données et tracé du graphique d'flèches

La deuxième étape consiste à définir les données et à tracer le graphique d'flèches à l'aide de la fonction `make_arrow_graph()`. Nous allons définir les données comme un dictionnaire avec les probabilités pour les bases et les transitions entre paires. Nous allons également définir la taille du graphique à 4 et normaliser les données.

```python
# Définition des données
data = {
    'A': 0.4, 'T': 0.3, 'G': 0.6, 'C': 0.2,
    'AT': 0.4, 'AC': 0.3, 'AG': 0.2,
    'TA': 0.2, 'TC': 0.3, 'TG': 0.4,
    'CT': 0.2, 'CG': 0.3, 'CA': 0.2,
    'GA': 0.1, 'GT': 0.4, 'GC': 0.1,
}

# Tracé du graphique d'flèches
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size)

plt.show()
```
