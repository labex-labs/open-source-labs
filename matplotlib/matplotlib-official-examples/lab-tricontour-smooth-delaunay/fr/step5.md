# Masquer certains triangles

Nous masquons certains des triangles du maillage pour simuler des données invalidées. Nous sélectionnons aléatoirement un sous-ensemble de triangles en fonction du paramètre `init_mask_frac`.

```python
# Certaines données invalides sont masquées
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
