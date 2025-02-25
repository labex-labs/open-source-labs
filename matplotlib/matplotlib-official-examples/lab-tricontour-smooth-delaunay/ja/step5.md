# 一部の三角形をマスクする

メッシュ内の一部の三角形をマスクして、無効なデータをシミュレートします。`init_mask_frac`パラメータに基づいて、三角形のサブセットをランダムに選択します。

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
