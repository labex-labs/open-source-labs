# Mask Some Triangles

We mask out some of the triangles in the mesh to simulate invalidated data. We randomly select a subset of triangles based on the `init_mask_frac` parameter.

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
