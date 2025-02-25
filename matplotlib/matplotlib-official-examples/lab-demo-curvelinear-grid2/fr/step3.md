# Définition de GridHelperCurveLinear

La troisième étape consiste à définir l'instance de GridHelperCurveLinear. Nous utiliserons les fonctions de transformation définies dans l'étape 2 pour transformer la grille. Nous définirons également `grid_locator1` et `grid_locator2` sur `MaxNLocator(nbins=6)` pour augmenter la densité des graduations.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
