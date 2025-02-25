# Créer une boîte de texte

```python
plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Nous créons une boîte de texte contenant le mot "eggs" à l'aide de la méthode `text()`. Le paramètre `bbox` est utilisé pour styliser la boîte. Le paramètre `boxstyle` est défini sur "round" pour créer une boîte arrondie, tandis que les paramètres `ec` et `fc` définissent respectivement les couleurs des bords et de la face de la boîte. Le paramètre `size` définit la taille de la police, le paramètre `rotation` définit l'angle de rotation, et les paramètres `ha` et `va` définissent l'alignement horizontal et vertical du texte dans la boîte.
