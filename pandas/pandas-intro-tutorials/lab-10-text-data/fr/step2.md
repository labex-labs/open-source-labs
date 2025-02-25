# Convertir les caractères de chaîne en minuscules

Ensuite, nous allons convertir tous les caractères de la colonne `Name` en minuscules. Nous utiliserons la méthode `str.lower()` pour y arriver.

```python
# Convertir tous les caractères de la colonne 'Name' en minuscules
titanic["Name"] = titanic["Name"].str.lower()
```
