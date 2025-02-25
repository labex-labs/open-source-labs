# Comprendre les conséquences des étiquettes dupliquées

Les étiquettes dupliquées peuvent modifier le comportement de certaines opérations dans pandas. Par exemple, certaines méthodes ne fonctionnent pas lorsqu'il y a des doublons.

```python
# Creating a pandas Series with duplicate labels
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Attempting to reindex the Series
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
