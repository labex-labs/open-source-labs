# Mascar Alguns Triângulos

Nós mascaramos alguns dos triângulos na malha para simular dados inválidos. Selecionamos aleatoriamente um subconjunto de triângulos com base no parâmetro `init_mask_frac`.

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
