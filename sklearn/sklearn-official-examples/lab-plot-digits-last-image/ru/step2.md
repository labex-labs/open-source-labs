# Визуализация набора данных

Для лучшего понимания набора данных мы можем визуализировать образец изображения с использованием matplotlib. Следующий код отображает последнюю цифру в наборе данных:

```python
import matplotlib.pyplot as plt

# Display the last digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```
