# Dessiner la ligne de connexion

La cinquième étape consiste à dessiner une ligne pointillée reliant les deux sous-graphiques. Nous créons un objet `ConnectionPatch` qui relie l'origine du sous-graphique de gauche au bord droit du sous-graphique de droite. Nous enregistrons également l'objet de patch `con`, que nous mettrons à jour plus tard dans l'animation.

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```
