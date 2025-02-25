# Generiere einen Plot

In diesem Schritt generieren wir einen Streudiagramm, indem wir das Dictionary `data` als Eingabe für die `scatter()`-Funktion verwenden. Wir werden die Zeichenketten, die den Variablen `a`, `b`, `c` und `d` entsprechen, verwenden, um den Plot zu generieren.

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='Eintrag a', ylabel='Eintrag b')
plt.show()
```
