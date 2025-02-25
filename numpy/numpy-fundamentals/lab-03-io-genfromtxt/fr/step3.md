# Découpage des lignes en colonnes

L'argument `delimiter` est utilisé pour définir comment les lignes doivent être découpées en colonnes. Par défaut, `numpy.genfromtxt` suppose que `delimiter=None`, ce qui signifie que la ligne est découpée selon les espaces blancs (y compris les tabulations).

```python
np.genfromtxt(StringIO(data), delimiter=",")
```
