# Plotten von Daten mit standardmäßigen Lücken an Wochenenden

Wir werden zunächst die Daten mit den standardmäßigen Lücken an Wochenenden mit der `plot`-Funktion in matplotlib plotten. Wir werden auch die Lücken in den täglichen Daten mit weißen durchgezogenen Linien hervorheben.

```python
# Plot data with gaps on weekends
fig, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(r.date, r.adj_close, 'o-')

# Highlight gaps in daily data
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, 'D'))
for gap in r[['date', 'adj_close']][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, 'w--', lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls='--', label='Gaps in daily data')])

ax1.set_title("Plotting Data with Default Gaps on Weekends")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter('%a'))
```
