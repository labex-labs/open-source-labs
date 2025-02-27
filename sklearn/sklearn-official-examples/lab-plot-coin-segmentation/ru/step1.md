# Загрузка и предобработка изображения

Начнем с загрузки изображения греческих монет и его предобработки, чтобы сделать его обработку проще. Мы уменьшим размер изображения до 20% от исходного и применим гауссовый фильтр для сглаживания перед уменьшением масштаба, чтобы уменьшить артефакты алиасинга.

```python
# load the coins as a numpy array
orig_coins = coins()

# Resize it to 20% of the original size to speed up the processing
# Applying a Gaussian filter for smoothing prior to down-scaling
# reduces aliasing artifacts.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
