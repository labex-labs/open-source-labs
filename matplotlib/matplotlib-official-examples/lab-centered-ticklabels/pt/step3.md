# Definir os Localizadores e Formatadores Principais e Secundários

Para centralizar os rótulos entre as marcas (ticks), precisamos definir os localizadores e formatadores principais e secundários para o eixo x. Usaremos a função `dates.MonthLocator()` para definir os localizadores principais e secundários para o mês e a função `dates.DateFormatter()` para formatar os rótulos das marcas secundárias para a abreviação do mês.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 é uma ligeira aproximação, pois os meses diferem no número de dias.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
