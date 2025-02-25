# Symlog-Plot auf sowohl der x- als auch der y-Achse erstellen

Im dritten Teilplot werden wir einen Symlog-Plot auf sowohl der x- als auch der y-Achse erstellen. Wir werden auch den Parameter `linthresh` auf 0,015 setzen.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
