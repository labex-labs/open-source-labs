# Définir une fonction

Maintenant, nous allons définir une fonction appelée `survey` qui prend en entrée les `results` et les `category_names` et crée une visualisation sous forme de diagramme en barres empilées horizontales.

```python
def survey(results, category_names):
    """
    Paramètres
    ----------
    results : dict
        Une correspondance entre les étiquettes des questions et une liste de réponses par catégorie.
        On suppose que toutes les listes contiennent le même nombre d'entrées et qu'elles correspondent à la longueur de *category_names*.
    category_names : list of str
        Les étiquettes des catégories.
    """
    # Convertir les résultats et les catégories en tableaux numpy
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # Calculer les sommes cumulatives des données pour l'empilement horizontal
    data_cum = data.cumsum(axis=1)

    # Définir les couleurs des catégories
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # Créer le graphique et définir les propriétés des axes
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.inverse_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # Créer les barres empilées et ajouter les étiquettes des barres
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # Ajouter la légende
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```
