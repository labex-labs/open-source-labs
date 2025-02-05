# Define GridHelperCurveLinear

The third step is to define the GridHelperCurveLinear instance. We will use the transformation functions defined in Step 2 to transform the grid. We will also set the `grid_locator1` and `grid_locator2` to `MaxNLocator(nbins=6)` to increase the tick density.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
