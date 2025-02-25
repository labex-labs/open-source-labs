# Den Plot erstellen

Jetzt können wir den Plot mit Matplotlib erstellen. Wir werden die `plot`-Funktion verwenden, um unsere Daten zu plotten, und die Grenzen der x-Achse mit der `set_xlim`-Funktion festlegen.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # abnehmende Zeit
ax.set_xlabel('abnehmende Zeit (s)')
ax.set_ylabel('Spannung (mV)')
ax.set_title('Sollte wachsen...')
ax.grid(True)

plt.show()
```
