# Настройте параметры по умолчанию

Для настройки параметров по умолчанию для определенного графика вы можете снова использовать метод `rcParams.update()`. На этот раз вы передадите словарь с именами параметров и значениями, которые вы хотите установить для этого графика. Вот пример, который настраивает некоторые параметры по умолчанию для определенного графика:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
