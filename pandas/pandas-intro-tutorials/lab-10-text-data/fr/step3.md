# Extraire les noms de famille des noms complets

Maintenant, créons une nouvelle colonne `Surname` qui contient le nom de famille des passagers. Nous y arriverons en extrayant la partie avant la virgule dans la colonne `Name`.

```python
# Divisez la colonne 'Name' sur la virgule et extrayez la première partie
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```
