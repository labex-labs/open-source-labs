# Meilleures pratiques de conception

Donnez toujours des noms courts, mais significatifs aux arguments des fonctions.

Quelqu'un utilisant une fonction peut vouloir utiliser le style d'appel avec arguments nommés.

```python
d = read_prices('prices.csv', debug=True)
```

Les outils de développement Python afficheront les noms dans les fonctionnalités d'aide et la documentation.
