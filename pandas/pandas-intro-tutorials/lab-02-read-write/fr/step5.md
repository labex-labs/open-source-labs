# Écriture des données dans un fichier Excel

Vous pouvez également écrire les données dans un fichier Excel en utilisant la méthode `to_excel`. Enregistrons notre DataFrame dans un fichier Excel.

```python
# Enregistrement du DataFrame dans un fichier Excel
titanic.to_excel("titanic.xlsx", sheet_name="passagers", index=False)
```
