# Tick-Labels mit ConciseFormatter formatieren

Wir werden die Tick-Labels auf dem zweiten Subplot mit dem ConciseFormatter formatieren.

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```
