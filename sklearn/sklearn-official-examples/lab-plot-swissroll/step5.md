# Generate Swiss-Hole Dataset

We generate the Swiss-Hole dataset by adding a hole to the Swiss Roll dataset using the `hole=True` parameter in the `make_swiss_roll()` function.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
