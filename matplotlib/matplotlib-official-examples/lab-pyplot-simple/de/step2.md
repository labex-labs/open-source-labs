# Erstellen eines einfachen Plots

Um in Matplotlib einen einfachen Plot zu erstellen, müssen Sie eine Liste von Zahlen angeben, die Sie plotten möchten. In diesem Fall werden wir eine Liste von Zahlen gegen ihren Index plotten, was zu einer geraden Linie führt. Verwenden Sie einen Formatstring (hier 'o-r'), um die Marker (Kreise), die Linienart (fester Strich) und die Farbe (rot) festzulegen.

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('einige Zahlen')
plt.show()
```
