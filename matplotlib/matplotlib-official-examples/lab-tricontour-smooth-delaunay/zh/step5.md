# 屏蔽一些三角形

我们在网格中屏蔽一些三角形，以模拟无效数据。我们根据 `init_mask_frac` 参数随机选择三角形的一个子集。

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
