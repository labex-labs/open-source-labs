# Legenden an komplexere Diagramme anfügen

In diesem Schritt werden wir Legenden an komplexere Diagramme anfügen.

```python
# Definiere Daten für das Diagramm
fig, axs = plt.subplots(3, 1, layout="constrained")
top_ax, middle_ax, bottom_ax = axs

# Erstelle ein Balkendiagramm mit mehreren Balken
top_ax.bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.4, label="Balken 1",
           align="center")
top_ax.bar([0.5, 1.5, 2.5], [0.3, 0.2, 0.2], color="rot", width=0.4,
           label="Balken 2", align="center")
top_ax.legend()

# Erstelle ein Fehlerbalkendiagramm mit mehreren Fehlern
middle_ax.errorbar([0, 1, 2], [2, 3, 1], xerr=0.4, fmt="s", label="test 1")
middle_ax.errorbar([0, 1, 2], [3, 2, 4], yerr=0.3, fmt="o", label="test 2")
middle_ax.errorbar([0, 1, 2], [1, 1, 3], xerr=0.4, yerr=0.3, fmt="^",
                   label="test 3")
middle_ax.legend()

# Erstelle ein Stabdiagramm mit einer Legende
bottom_ax.stem([0.3, 1.5, 2.7], [1, 3.6, 2.7], label="Stabtest")
bottom_ax.legend()

# Zeige das Diagramm an
plt.show()
```
