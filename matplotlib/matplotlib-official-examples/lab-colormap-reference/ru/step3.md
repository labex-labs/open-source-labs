# Использование встроенных цветовых карты

Matplotlib предоставляет широкий выбор встроенных цветовых карты, которые можно использовать для представления данных. Эти цветовые карты можно получить по их именам, перечисленным в модуле `matplotlib.cm`.

```python
import matplotlib.pyplot as plt

# Создайте график с использованием цветовой карты 'viridis'
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
