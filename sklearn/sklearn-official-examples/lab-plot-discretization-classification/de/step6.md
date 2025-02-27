# Ergebnisse visualisieren

In diesem Schritt werden wir die Ergebnisse des Feature-Diskretisierungsprozesses visualisieren. Wir werden die Klassifikationsgenauigkeit auf dem Testset für jeden Klassifizierer und Datensatz plotten.

```python
plt.tight_layout()

# Fügen Sie Überschriften über der Abbildung hinzu
plt.subplots_adjust(top=0.90)
Überschriften = [
    "Lineare Klassifizierer",
    "Feature-Diskretisierung und lineare Klassifizierer",
    "Nicht-lineare Klassifizierer",
]
für i, Überschrift in zip([1, 3, 5], Überschriften):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        Überschrift,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```
