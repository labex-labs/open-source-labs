# Generieren von Daten für das Streudiagramm

Als nächstes generieren wir die Daten für das Streudiagramm. Wir erstellen 100 Datenpunkte mit zufälligen x- und y-Werten zwischen 0 und 0,9 und zufälligen Radien zwischen 0 und 10. Die Farbe jedes Datenpunkts wird durch die Quadratwurzel seiner Fläche bestimmt.

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 bis 10 Punktradien
c = np.sqrt(area)
```
