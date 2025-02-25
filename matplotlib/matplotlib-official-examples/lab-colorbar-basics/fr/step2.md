# Générer des données

Nous générons quelques données d'échantillonnage pour le tracé, en utilisant la fonction `mgrid` de `numpy`.

```python
# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
