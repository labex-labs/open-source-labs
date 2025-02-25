# Alle übereinstimmenden Indizes finden

## Problem

Schreiben Sie eine Funktion `find_index_of_all(lst, fn)`, die eine Liste `lst` und eine Testfunktion `fn` als Argumente nimmt und eine Liste von Indizes aller Elemente in `lst` zurückgibt, für die `fn` `True` zurückgibt.

### Eingabe

- Eine Liste `lst` von ganzen Zahlen.
- Eine Testfunktion `fn`, die eine ganze Zahl als Eingabe nimmt und einen booleschen Wert zurückgibt.

### Ausgabe

- Eine Liste von ganzen Zahlen, die die Indizes aller Elemente in `lst` repräsentieren, für die `fn` `True` zurückgibt.

## Beispiel

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
find_index_of_all([1, 2, 3, 4], lambda n: n > 2) # [2, 3]
find_index_of_all([1, 2, 3, 4], lambda n: n < 0) # []
```

### Hinweis

- Im ersten Beispiel überprüft die Testfunktion `lambda n: n % 2 == 1`, ob die ganze Zahl ungerade ist. Die Funktion gibt `[0, 2]` zurück, weil die Elemente an den Indizes `0` und `2` der Liste `[1, 2, 3, 4]` ungerade sind.
- Im zweiten Beispiel überprüft die Testfunktion `lambda n: n > 2`, ob die ganze Zahl größer als `2` ist. Die Funktion gibt `[2, 3]` zurück, weil die Elemente an den Indizes `2` und `3` der Liste `[1, 2, 3, 4]` größer als `2` sind.
- Im dritten Beispiel überprüft die Testfunktion `lambda n: n < 0`, ob die ganze Zahl negativ ist. Die Funktion gibt `[]` zurück, weil es keine negativen Elemente in der Liste `[1, 2, 3, 4]` gibt.
