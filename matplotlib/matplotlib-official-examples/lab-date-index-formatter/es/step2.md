# Representación gráfica de datos con espacios en blanco predeterminados los fines de semana

En primer lugar, representaremos los datos con los espacios en blanco predeterminados los fines de semana utilizando la función `plot` de matplotlib. También destacaremos los espacios en blanco en los datos diarios utilizando líneas discontinuas en blanco.

```python
# Representación gráfica de datos con espacios en blanco los fines de semana
fig, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(r.date, r.adj_close, 'o-')

# Destacar los espacios en blanco en los datos diarios
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, 'D'))
for gap in r[['date', 'adj_close']][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, 'w--', lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls='--', label='Espacios en blanco en los datos diarios')])

ax1.set_title("Representación gráfica de datos con espacios en blanco predeterminados los fines de semana")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter('%a'))
```
