# Convert Column Labels to Lowercase

Finally, we'll convert the column labels to lowercase using a function.

```python
# Convert column labels to lowercase
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
```
