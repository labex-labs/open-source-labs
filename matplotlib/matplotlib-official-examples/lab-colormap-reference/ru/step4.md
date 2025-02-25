# Переворачивание цветовых карты

Matplotlib позволяет перевернуть цветовую карту, добавив `_r` к имени цветовой карты.

```python
import matplotlib.pyplot as plt

# Создайте график с использованием перевернутой цветовой карты 'viridis'
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
