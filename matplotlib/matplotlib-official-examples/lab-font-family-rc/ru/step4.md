# Выбор конкретного моноширинного шрифта

Если мы хотим использовать конкретный моноширинный шрифт, мы можем установить параметр `font.monospace` в список имен шрифтов. Matplotlib попытается использовать первый шрифт из списка, доступный на системе пользователя. Для этого мы можем использовать следующий код:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```
