# Erstellen des Gitters

Als nächstes werden wir das Gitter in Polarkoordinaten erstellen und die entsprechende Z berechnen. Wir werden ein Array von Radiuswerten `r`, ein Array von Winkelwerten `p` erstellen und dann die `meshgrid()`-Funktion von NumPy verwenden, um ein Gitter von `R`- und `P`-Werten zu erstellen. Schließlich werden wir die `Z`-Gleichung verwenden, um die Höhe jedes Punktes auf der Oberfläche zu berechnen.

```python
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
```
