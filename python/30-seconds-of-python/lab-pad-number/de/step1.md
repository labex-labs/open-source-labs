# Zahl auffüllen

Schreiben Sie eine Funktion `pad_number(n, l)`, die eine Zahl `n` und eine Länge `l` als Eingabe nimmt und einen String zurückgibt, der die aufgefüllte Zahl darstellt. Die Funktion sollte die Zahl mit führenden Nullen auffüllen, um sie `l` Stellen lang zu machen. Wenn die Zahl bereits `l` Stellen lang ist, sollte die Funktion die Zahl als String zurückgeben.

Um die Zahl aufzufüllen, können Sie die `str.zfill()`-Methode verwenden. Diese Methode nimmt eine Länge als Eingabe und füllt den String mit führenden Nullen, bis er diese Länge hat. Beispielsweise würde `"7".zfill(6)` `"000007"` zurückgeben.

```python
def pad_number(n, l):
  return str(n).zfill(l)
```

```python
pad_number(1234, 6); # '001234'
```
