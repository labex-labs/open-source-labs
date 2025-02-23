# Создание базового графика

Попробуем создать базовый график с текстовым элементом. В своем скрипте на Python добавьте следующий код:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```
