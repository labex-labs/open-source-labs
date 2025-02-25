# Definieren der Daten

Als nächstes müssen wir die Daten definieren, die wir für unser Diagramm verwenden werden. Wir werden eine Sinuswelle mit 201 Datenpunkten erstellen:

```python
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)
```
