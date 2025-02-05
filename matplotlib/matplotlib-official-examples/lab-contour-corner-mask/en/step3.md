# Masking the Data

In this step, we will mask some of the `z` values using a Boolean mask. We create a `mask` array using the `np.zeros_like()` function, and then set some of the values to `True` to mask them.

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
