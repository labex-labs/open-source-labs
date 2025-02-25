# Tracer le texte

Maintenant que nous avons défini le texte, nous pouvons le tracer à l'aide de Matplotlib. Dans cette étape, nous créons une figure et ajoutons le texte à l'aide de la méthode `fig.text()`.

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i +.5) / len(tests), s, fontsize=32)

plt.show()
```
