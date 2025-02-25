# Скрыть некоторые треугольники

Мы скрываем некоторые треугольники в сетке, чтобы имитировать недействительные данные. Мы случайным образом выбираем подмножество треугольников на основе параметра `init_mask_frac`.

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
