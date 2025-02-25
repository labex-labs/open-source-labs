# Erstellen eines Plots mit Mercator-Transformationsskala

Als Bonus werden wir auch einen Plot erstellen, der die Mercator-Transformationsfunktion verwendet. Dies ist keine integrierte Funktion in Matplotlib, aber wir können unsere eigenen Vorwärts- und Rückwärtstransformationsfunktionen definieren, um einen Plot mit Mercator-Transformationsskala zu erstellen. In diesem Beispiel werden wir die `forward()`- und `inverse()`-Funktionen für die Mercator-Transformation definieren. Wir fügen auch einen Titel und ein Gitter zum Plot hinzu.

```python
# Funktion Mercator-Transformation
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
