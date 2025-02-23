# 2D-Daten auf dem 3D-Diagramm darstellen

Der dritte Schritt besteht darin, 2D-Daten auf dem 3D-Diagramm mit `ax.plot` und `ax.scatter` darzustellen. Die `ax.plot`-Funktion zeichnet eine Sinus-Kurve mit den x- und y-Achsen. Die `ax.scatter`-Funktion zeichnet Streudiagrammdaten auf den x- und z-Achsen.

```python
# Zeichnet eine Sinus-Kurve mit den x- und y-Achsen.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# Zeichnet Streudiagrammdaten (20 2D-Punkte pro Farbe) auf den x- und z-Achsen.
colors = ('r', 'g', 'b', 'k')

# Fixiert den Zufallszustand für die Reproduzierbarkeit
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# Indem man zdir='y' verwendet, wird der y-Wert dieser Punkte auf den zs-Wert 0 festgelegt
# und die (x, y)-Punkte werden auf den x- und z-Achsen gezeichnet.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')
```
