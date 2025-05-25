# Definir o eixo x e formatar as datas

Para tornar o gráfico mais legível, definiremos os limites do eixo x para a primeira e a última datas do intervalo. Também definiremos os localizadores principais e secundários para DayLocator e HourLocator, respectivamente. Finalmente, formataremos as datas usando a função DateFormatter. Copie e cole o seguinte código:

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
