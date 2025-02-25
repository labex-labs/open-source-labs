# Réinitialiser les options

Si nous souhaitons réinitialiser une ou plusieurs options à leur valeur par défaut, nous pouvons utiliser `pd.reset_option`.

```python
# Réinitialisez le nombre maximum de lignes à afficher à la valeur par défaut
pd.reset_option("display.max_rows")

# Vérifiez la réinitialisation
print(pd.options.display.max_rows)
```
