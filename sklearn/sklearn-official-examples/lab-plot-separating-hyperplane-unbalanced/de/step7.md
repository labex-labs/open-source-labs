# Legende hinzufügen

Wir werden der Grafik eine Legende hinzufügen, indem wir die `legend`-Funktion aus `matplotlib.pyplot` verwenden. Wir werden die Beschriftungen auf `"nicht gewichtet"` und `"gewichtet"` setzen.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```
