# Zeichnen der Zielverteilungen für die Ames Wohnungsdaten

Wir zeichnen die Wahrscheinlichkeitsdichtefunktionen des Ziels vor und nach der Anwendung des QuantileTransformers.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_ylabel("Wahrscheinlichkeit")
ax0.set_xlabel("Ziel")
ax0.set_title("Zielverteilung")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("Wahrscheinlichkeit")
ax1.set_xlabel("Ziel")
ax1.set_title("Transformierte Zielverteilung")

f.suptitle("Ames Wohnungsdaten: Verkaufspreis", y=1.05)
plt.tight_layout()
```
