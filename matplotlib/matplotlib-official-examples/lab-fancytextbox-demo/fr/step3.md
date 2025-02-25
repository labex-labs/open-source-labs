# Créer une autre boîte de texte

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Nous créons une autre boîte de texte contenant le mot "spam". Cette fois, nous définissons le paramètre `boxstyle` sur "square" pour créer une boîte carrée et les paramètres `ha` et `va` sur "right" et "top" pour aligner le texte à droite et en haut de la boîte.
