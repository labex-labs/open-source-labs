# Definieren von GridHelperCurveLinear

Der dritte Schritt besteht darin, die GridHelperCurveLinear-Instanz zu definieren. Wir werden die in Schritt 2 definierten Transformationsfunktionen verwenden, um das Gitter zu transformieren. Wir werden auch `grid_locator1` und `grid_locator2` auf `MaxNLocator(nbins=6)` setzen, um die Strichdichte zu erhöhen.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
