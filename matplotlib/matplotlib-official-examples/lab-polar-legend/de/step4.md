# Daten plotten

Jetzt können wir unsere Daten mit der `plot`-Funktion plotten. Wir werden zwei Linien mit den Daten erstellen, die wir im Schritt 3 erstellt haben.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
