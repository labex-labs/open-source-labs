# Traçage des données avec des trous par défaut le week-end

Nous allons tout d'abord tracer les données avec les trous par défaut le week-end en utilisant la fonction `plot` de matplotlib. Nous mettrons également en évidence les trous dans les données quotidiennes en utilisant des lignes pointillées blanches.

```python
# Tracer les données avec des trous le week-end
fig, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(r.date, r.adj_close, 'o-')

# Mettre en évidence les trous dans les données quotidiennes
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, 'D'))
for gap in r[['date', 'adj_close']][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, 'w--', lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls='--', label='Gaps in daily data')])

ax1.set_title("Plotting Data with Default Gaps on Weekends")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter('%a'))
```
