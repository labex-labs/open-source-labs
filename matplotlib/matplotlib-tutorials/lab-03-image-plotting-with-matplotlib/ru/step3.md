# Применение псевдоцветовых схем

Псевдоцветовые схемы можно использовать для повышения контраста и более легкого визуализации данных. Если изображение является оттеночным, мы можем применить псевдоцветовые схемы, указав различные цветовые карты. Мы можем сделать это, используя параметр `cmap` в функции `imshow`.

```python
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
```
