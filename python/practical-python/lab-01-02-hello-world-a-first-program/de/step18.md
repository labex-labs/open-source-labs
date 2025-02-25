# Übung 1.5: Der springende Ball

Ein Gummiball wird von einer Höhe von 100 Metern fallen gelassen und springt jedes Mal, wenn er den Boden trifft, auf 3/5 der Höhe zurück, von der er gefallen ist. Schreiben Sie ein Programm `bounce.py`, das eine Tabelle druckt, die die Höhe der ersten 10 Bounces zeigt.

Hier ist eine Lösung:

```python
# bounce.py

height = 100
bounce = 1
while bounce <= 10:
    height = height * (3 / 5)
    print(bounce, round(height, 4))
    bounce += 1
```

Ihr Programm sollte eine Tabelle erzeugen, die ungefähr so aussieht:

```code
1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
```

_Hinweis: Sie können die Ausgabe etwas aufräumen, wenn Sie die round()-Funktion verwenden. Versuchen Sie, die Ausgabe auf 4 Stellen zu runden._

```code
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
```
