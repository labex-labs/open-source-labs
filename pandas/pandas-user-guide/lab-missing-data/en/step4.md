# Perform Calculations with Missing Data

We'll perform some basic arithmetic and statistical calculations with missing data.

```python
# Perform calculations with missing data
df["one"].sum()
df.mean(axis=1, numeric_only=True)
df.cumsum()
```
