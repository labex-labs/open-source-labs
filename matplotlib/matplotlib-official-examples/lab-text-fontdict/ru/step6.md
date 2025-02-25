# Настраиваем подписи осей

Мы также можем настроить подписи осей нашего графика с использованием словаря шрифта. Мы укажем параметр fontdict функций xlabel() и ylabel() равным нашему словарю шрифта.

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
