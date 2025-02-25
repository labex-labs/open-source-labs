# Crear gráficos

En este paso, crearemos dos gráficos: uno usando unidades personalizadas y el otro usando unidades predeterminadas.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Unidades personalizadas")
fig.subplots_adjust(bottom=0.2)

# graficar especificando unidades
ax2.plot(x, y, 'o', xunits=2.0)
ax2.set_title("xunits = 2.0")
plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')

# graficar sin especificar unidades; usará la rama None para axisinfo
ax1.plot(x, y)  # usa unidades predeterminadas
ax1.set_title('unidades predeterminadas')
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

plt.show()
```
