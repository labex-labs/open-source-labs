# Установка пределов и меток осей

Мы установим пределы и метки для осей x и y для каждой оси с использованием функции `set()`.

```python
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```
