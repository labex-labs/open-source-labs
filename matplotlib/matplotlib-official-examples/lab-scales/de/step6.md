# Erstellen eines Plots mit benutzerdefinierter Skala

Die letzte Art von Skalierungsumformung, die wir untersuchen werden, ist die benutzerdefinierte Skala. Dies ermöglicht es uns, unsere eigenen Funktionen für die Vorwärts- und Rückwärtstransformation der Skalierung zu definieren. In diesem Beispiel werden wir eine benutzerdefinierte Funktion definieren, um die Quadratwurzel der Daten zu berechnen. Um einen Plot mit benutzerdefinierter Skala zu erstellen, verwenden wir die Methode `set_yscale()` und übergeben den String `'function'`. Wir definieren auch die Funktionen `forward()` und `inverse()` und übergeben sie als Argumente an den Parameter `functions`. Wir fügen auch einen Titel und ein Gitter zum Plot hinzu.

```python
# Funktion x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```
