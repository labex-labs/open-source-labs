# Ajuster la conversion

L'argument `converters` nous permet de définir des fonctions de conversion pour gérer des conversions plus complexes. Il accepte un dictionnaire avec les indices de colonne ou les noms de colonne comme clés et les fonctions de conversion comme valeurs.

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```
