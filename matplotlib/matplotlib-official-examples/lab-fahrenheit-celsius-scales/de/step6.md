# Festlegen der Achsengrenzen und -beschriftungen

Wir legen die Grenzen der x-Achse auf (0,100) fest und geben die y-Achsenbeschriftungen und den Titel an.

```python
ax_f.set_xlim(0, 100)
ax_f.set_title('Two scales: Fahrenheit and Celsius')
ax_f.set_ylabel('Fahrenheit')
ax_c.set_ylabel('Celsius')
```
