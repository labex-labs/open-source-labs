# Устанавливаем метки делений по оси y по умолчанию справа

Мы можем установить метки делений по оси y по умолчанию справа от графика с помощью следующего кода:

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```
