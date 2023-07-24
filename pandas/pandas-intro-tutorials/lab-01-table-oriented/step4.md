# Perform Basic Statistics

Pandas provides a lot of functionalities to perform statistics. For instance, you can find the maximum value in a column using `max()`.

```python
# Finding the maximum age
df["Age"].max()
```

You can also get a quick overview of the numerical data in a DataFrame using `describe()`.

```python
# Describing the numerical data
df.describe()
```
