# Plotando Dados com Lacunas Padrão nos Fins de Semana

Primeiramente, plotaremos os dados com as lacunas padrão nos fins de semana usando a função `plot` em matplotlib. Também destacaremos as lacunas nos dados diários usando linhas tracejadas brancas.

```python
# Plot data with gaps on weekends
fig, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(r.date, r.adj_close, 'o-')

# Highlight gaps in daily data
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, 'D'))
for gap in r[['date', 'adj_close']][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, 'w--', lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls='--', label='Gaps in daily data')])

ax1.set_title("Plotando Dados com Lacunas Padrão nos Fins de Semana")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter('%a'))
```
