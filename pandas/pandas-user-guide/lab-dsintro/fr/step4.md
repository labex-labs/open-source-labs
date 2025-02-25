# Manipulation des colonnes d'un DataFrame

Vous pouvez effectuer diverses opérations sur les colonnes d'un DataFrame. Par exemple, vous pouvez sélectionner une colonne, ajouter une nouvelle colonne ou supprimer une colonne.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
