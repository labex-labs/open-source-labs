# Die Z-Achse anpassen

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

Wir passen die Z-Achse an, indem wir die `set_zlim()`-Funktion verwenden, um die Grenzen der Z-Achse auf -1,01 bis 1,01 festzulegen. Anschließend verwenden wir die `set_major_locator()`-Funktion, um die Anzahl der Striche auf der Z-Achse auf 10 zu setzen, indem wir `LinearLocator(10)` verwenden. Schließlich verwenden wir die `set_major_formatter()`-Funktion, um die Beschriftungen der Striche auf der Z-Achse mit einem `StrMethodFormatter` zu formatieren.
