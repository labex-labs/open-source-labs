# Создать симметричный логарифмический график по оси x

В первом подграфике мы создадим симметричный логарифмический график по оси x. Также добавим мелкую сетку по оси x.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```
