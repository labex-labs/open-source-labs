# Conversion d'un tableau structuré en tableau enregistrement

Nous pouvons convertir un tableau structuré en tableau enregistrement en utilisant la méthode `view` et en spécifiant le type `np.recarray`.

```python
# Convertit un tableau structuré en tableau enregistrement
recordarr = x.view(np.recarray)
```
