# Insérer du texte dans le graphique

Ensuite, nous allons insérer du texte dans le graphique à l'aide de la fonction `text()`. Nous utiliserons le paramètre `math_fontfamily` pour changer la famille de polices pour chaque élément de texte individuel.

```python
# Un texte mélangeant du texte normal et du texte mathématique.
msg = (r"Texte normal. $Texte\ en\ mode mathématique:\ "
       r"\int_{0}^{\infty } x^2 dx$")

# Insérer le texte dans le graphique.
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# Utiliser une autre police pour le prochain texte.
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
