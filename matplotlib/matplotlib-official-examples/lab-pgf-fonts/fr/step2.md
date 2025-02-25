# Spécifiez la famille de polices

Nous allons définir la famille de polices sur "serif" en utilisant le paramètre `font.family`. De plus, nous allons définir le paramètre `font.serif` sur une liste vide pour utiliser la police serif LaTeX par défaut.

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```
