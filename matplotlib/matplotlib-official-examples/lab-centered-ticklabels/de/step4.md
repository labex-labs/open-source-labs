# Entferne die Hauptstrichbeschriftungen und die Zwischenstriche

Um das Verhalten zu simulieren, die Beschriftungen zwischen den Strichen zu zentrieren, müssen wir die Hauptstrichbeschriftungen und die Zwischenstriche entfernen und nur die Nebenstrichbeschriftungen anzeigen. Wir können dies mit der `tick_params()`-Funktion tun und die Parameter `tick1On` und `tick2On` auf `False` setzen.

```python
# Entferne die Strichlinien
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
