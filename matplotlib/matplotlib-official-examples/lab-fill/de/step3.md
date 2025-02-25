# Ein gefülltes Polygon generieren

Jetzt können wir ein gefülltes Polygon mit der `fill()`-Funktion generieren. Wir werden die Koch-Flocken-Funktion verwenden, um die Koordinaten für das Polygon zu generieren.

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
