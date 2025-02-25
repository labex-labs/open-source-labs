# Liste aufklappen

Ihre Aufgabe ist es, die Funktion `unfold` zu implementieren, die als Argumente eine Iterationsfunktion und einen initialen Startwert annimmt. Die Iterationsfunktion akzeptiert ein Argument (`seed`) und muss immer eine Liste mit zwei Elementen (`[value`, `nextSeed]`) zurückgeben oder `False`, um zu beenden. Die `unfold`-Funktion sollte eine Generatorfunktion `fn_generator` verwenden, die eine `while`-Schleife verwendet, um die Iterationsfunktion aufzurufen und den `value` auszugeben, bis sie `False` zurückgibt. Schließlich sollte die `unfold`-Funktion eine Listenkomprehension verwenden, um die Liste zurückzugeben, die vom Generator erzeugt wird, indem die Iterationsfunktion verwendet wird.

Implementieren Sie die `unfold`-Funktion:

```python
def unfold(fn, seed):
    # Ihr Code hier
```

### Eingabe

- Eine Iterationsfunktion `fn`, die ein Argument (`seed`) akzeptiert und immer eine Liste mit zwei Elementen (`[value`, `nextSeed]`) zurückgeben oder `False`, um zu beenden.
- Ein initialer Startwert `seed`.

### Ausgabe

- Eine Liste, die vom Generator erzeugt wird, indem die Iterationsfunktion verwendet wird.

```python
def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
```

```python
f = lambda n: False if n > 50 else [-n, n + 10]
unfold(f, 10) # [-10, -20, -30, -40, -50]
```
