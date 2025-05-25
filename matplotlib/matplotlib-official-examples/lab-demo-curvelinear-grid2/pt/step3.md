# Definir GridHelperCurveLinear

O terceiro passo é definir a instância `GridHelperCurveLinear`. Usaremos as funções de transformação definidas no Passo 2 para transformar a grade. Também definiremos `grid_locator1` e `grid_locator2` como `MaxNLocator(nbins=6)` para aumentar a densidade dos ticks.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
