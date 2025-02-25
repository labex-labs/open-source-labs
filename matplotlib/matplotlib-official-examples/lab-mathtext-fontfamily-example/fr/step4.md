# Définir la police pour le titre

Nous pouvons également changer la famille de polices pour le titre à l'aide du paramètre `math_fontfamily`.

```python
ax.set_title(r"$Titre\ en\ mode mathématique:\ \int_{0}^{\infty } x^2 dx$",
             math_fontfamily='stixsans', size=14)
```
