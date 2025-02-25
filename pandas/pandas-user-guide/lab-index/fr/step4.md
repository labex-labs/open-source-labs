# Travailler avec les données manquantes

Pandas fournit diverses méthodes pour nettoyer les données et remplir les valeurs manquantes.

```python
# Creating a DataFrame with missing values
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# Filling missing values
df.fillna(value=0, inplace=True)
```
