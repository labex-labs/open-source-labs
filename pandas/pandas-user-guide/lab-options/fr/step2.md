# Obtenir et définir des options

Nous pouvons obtenir ou définir la valeur d'une option unique en utilisant respectivement `pd.get_option` ou `pd.set_option`. Ici, nous définissons le nombre maximum de lignes à afficher sur 999.

```python
# Obtenez la configuration actuelle pour le nombre maximum de lignes à afficher
print(pd.options.display.max_rows)

# Définissez le nombre maximum de lignes à afficher sur 999
pd.options.display.max_rows = 999

# Vérifiez la nouvelle configuration
print(pd.options.display.max_rows)
```
