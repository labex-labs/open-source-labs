# Extraire des données spécifiques sur les passagers

Ensuite, extrayons les données sur les passagers qui étaient des comtesses à bord du Titanic. Nous utiliserons la méthode `str.contains()` pour trouver les lignes où la colonne `Name` contient le mot 'Countess'.

```python
# Trouvez les lignes où 'Name' contient 'Countess'
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
