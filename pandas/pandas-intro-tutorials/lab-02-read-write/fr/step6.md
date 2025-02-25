# Lecture des données à partir d'un fichier Excel

La lecture des données à partir d'un fichier Excel est aussi facile que la lecture des données à partir d'un fichier CSV. Nous utiliserons la fonction `read_excel` de pandas.

```python
# Lecture des données à partir d'un fichier Excel
titanic = pd.read_excel("titanic.xlsx", sheet_name="passagers")
```
