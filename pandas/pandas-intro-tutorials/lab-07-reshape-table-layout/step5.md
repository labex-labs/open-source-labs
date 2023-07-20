# Convert Wide to Long Format

Now, let's convert the wide format data of 𝑁𝑂2 to long format using the `melt` function.

```python
# Reset index for no2_pivoted
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# Melt the data
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
