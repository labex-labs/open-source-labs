# Задаем шрифт Matplotlib

Нам необходимо задать шрифт, который будет использоваться для текста Matplotlib. Мы будем использовать шрифт Computer Modern и установить его в качестве стандартного шрифта для Matplotlib.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
