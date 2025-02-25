# Préparer les données

Ensuite, nous allons préparer les données pour notre graphique. Nous avons trois espèces de pingouins et trois attributs, donc nous allons créer un dictionnaire avec les moyennes de chaque attribut par espèce.

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```
