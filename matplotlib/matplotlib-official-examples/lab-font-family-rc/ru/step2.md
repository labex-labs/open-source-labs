# Выбор конкретного шрифта без засечек

Если мы хотим использовать конкретный шрифт без засечек, мы можем установить параметр `font.sans-serif` в список имен шрифтов. Matplotlib попытается использовать первый шрифт из списка, доступный на системе пользователя. Для этого мы можем использовать следующий код:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```
