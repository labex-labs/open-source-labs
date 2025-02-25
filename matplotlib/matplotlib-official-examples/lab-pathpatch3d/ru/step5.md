# Напишем формулу LaTeX на полу

Мы напишем формулу LaTeX на полу `z = 0` трехмерного графика с использованием функции `text3d`.

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
