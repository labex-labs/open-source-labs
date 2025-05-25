# Formatar os rótulos de marcação usando o formatador conciso

Formataremos os rótulos de marcação no segundo subplot usando o formatador conciso.

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```
