# Comprendre le scalaire NA pour désigner les valeurs manquantes

Enfin, nous allons discuter du scalaire expérimental `NA` dans pandas qui peut être utilisé pour désigner les valeurs manquantes.

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```
