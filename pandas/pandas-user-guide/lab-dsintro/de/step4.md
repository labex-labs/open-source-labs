# Manipulieren von DataFrame-Spalten

Sie können verschiedene Operationen auf DataFrame-Spalten ausführen. Beispielsweise können Sie eine Spalte auswählen, eine neue Spalte hinzufügen oder eine Spalte löschen.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
