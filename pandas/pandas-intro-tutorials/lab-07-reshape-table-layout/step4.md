# Create a Pivot Table

Create a pivot table to find the mean concentrations for 𝑁𝑂2 and 𝑃𝑀25 in each of the stations.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```
