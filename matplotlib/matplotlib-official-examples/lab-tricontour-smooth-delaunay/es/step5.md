# Ocultar algunos triángulos

Ocultamos algunos de los triángulos de la malla para simular datos invalidados. Seleccionamos aleatoriamente un subconjunto de triángulos basado en el parámetro `init_mask_frac`.

```python
# Algunos datos no válidos se ocultan
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
