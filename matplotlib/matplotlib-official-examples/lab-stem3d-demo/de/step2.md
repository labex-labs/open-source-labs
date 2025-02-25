# Definieren der Daten

In diesem Schritt definieren wir die Daten, die wir verwenden werden, um das 3D-Stammdiagramm zu erstellen. Wir werden ein `linspace`-Array für den Winkel erstellen und die Sinus- und Kosinusfunktionen verwenden, um die x- und y-Koordinaten zu berechnen. Wir definieren auch die z-Koordinate als den Winkel.

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```
