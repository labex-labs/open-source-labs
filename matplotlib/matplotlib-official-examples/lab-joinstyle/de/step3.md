# Einstellen von JoinStyle

Wir können den `JoinStyle` der Linie mit der Methode `set_solid_joinstyle()` des `Line2D`-Objekts einstellen. Wir werden ein neues Linienobjekt erstellen und seinen Verbindungsstil auf `JoinStyle.bevel` setzen.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
