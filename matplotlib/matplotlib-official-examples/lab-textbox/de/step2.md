# Erstellen des Anfangsplots

Als nächstes erstellen wir den Anfangsplot, der sich basierend auf der Benutzereingabe aktualisieren wird. In diesem Beispiel erstellen wir einen Plot einer Funktion mit `t` als unabhängige Variable.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```
