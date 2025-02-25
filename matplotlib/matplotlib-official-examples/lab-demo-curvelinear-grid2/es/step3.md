# Definir GridHelperCurveLinear

El tercer paso es definir la instancia de GridHelperCurveLinear. Usaremos las funciones de transformación definidas en el Paso 2 para transformar la cuadrícula. También estableceremos `grid_locator1` y `grid_locator2` en `MaxNLocator(nbins=6)` para aumentar la densidad de las marcas de graduación.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
