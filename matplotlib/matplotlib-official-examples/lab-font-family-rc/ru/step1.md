# Выбор стандартного шрифта без засечек

Стандартным семейством шрифтов в Matplotlib является шрифт без засечек. Мы можем выбрать использовать стандартное семейство шрифтов, установив параметр `font.family` в `'sans-serif'`. Для этого мы можем использовать следующий код:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
```
