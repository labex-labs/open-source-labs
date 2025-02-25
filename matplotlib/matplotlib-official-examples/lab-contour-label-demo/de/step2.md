# Erstellen von Konturbeschriftungen mit benutzerdefinierten Levelformatter

Wir werden nun Konturbeschriftungen mit benutzerdefinierten Levelformatter erstellen. Dies wird uns ermöglichen, die Beschriftungen auf eine bestimmte Weise zu formatieren. In diesem Fall werden wir die Nachkommastellen abschneiden und ein Prozentzeichen hinzufügen.

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```
