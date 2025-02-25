# Создать симметричный логарифмический график по обеим осям x и y

В третьем подграфике мы создадим симметричный логарифмический график по обеим осям x и y. Также установим параметр `linthresh` равным 0,015.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
