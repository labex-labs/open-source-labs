# Interpoler les valeurs manquantes

Nous utiliserons la fonction `interpolate` pour remplir les valeurs manquantes dans un DataFrame.

```python
df = pd.DataFrame(
   {
       "A": [1, 2.1, np.nan, 4.7, 5.6, 6.8],
       "B": [0.25, np.nan, np.nan, 4, 12.2, 14.4],
   }
)
df.interpolate()
```
