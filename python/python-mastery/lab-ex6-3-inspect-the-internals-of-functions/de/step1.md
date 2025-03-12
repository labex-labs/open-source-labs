# Untersuchung von Funktionsattributen

In Python werden Funktionen als First-Class-Objekte (erstklassige Objekte) betrachtet. Was bedeutet das? Nun, es ist ähnlich wie in der realen Welt, wo es verschiedene Arten von Objekten gibt, wie z.B. ein Buch oder einen Stift. In Python sind auch Funktionen Objekte, und wie andere Objekte verfügen sie auch über ihre eigenen Attribute. Diese Attribute können uns viele nützliche Informationen über die Funktion geben, wie z.B. ihren Namen, wo sie definiert ist und wie sie implementiert ist.

Lassen Sie uns unsere Untersuchung beginnen, indem wir eine interaktive Python-Shell öffnen. Diese Shell ist wie ein Spielplatz, auf dem wir sofort Python-Code schreiben und ausführen können. Dazu navigieren wir zunächst in das Projektverzeichnis und starten dann den Python-Interpreter. Hier sind die Befehle, die Sie in Ihrem Terminal ausführen müssen:

```bash
cd ~/project
python3
```

Jetzt, da wir in der interaktiven Python-Shell sind, definieren wir eine einfache Funktion. Diese Funktion nimmt zwei Zahlen und addiert sie. So können wir sie definieren:

```python
def add(x, y):
    'Adds two things'
    return x + y
```

In diesem Code haben wir eine Funktion namens `add` erstellt. Sie nimmt zwei Parameter, `x` und `y`, und gibt ihre Summe zurück. Die Zeichenkette `'Adds two things'` wird Docstring genannt, der verwendet wird, um zu dokumentieren, was die Funktion tut.

## Verwendung von `dir()` zur Untersuchung von Funktionsattributen

In Python ist die `dir()`-Funktion ein nützliches Werkzeug. Sie kann verwendet werden, um eine Liste aller Attribute und Methoden eines Objekts zu erhalten. Lassen Sie uns sie verwenden, um zu sehen, welche Attribute unsere `add`-Funktion hat. Führen Sie den folgenden Code in der interaktiven Python-Shell aus:

```python
dir(add)
```

Wenn Sie diesen Code ausführen, sehen Sie eine lange Liste von Attributen. Hier ist ein Beispiel für die Ausgabe:

```
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

Diese Liste zeigt alle Attribute und Methoden, die mit der `add`-Funktion verbunden sind.

## Zugriff auf grundlegende Funktionsinformationen

Jetzt schauen wir uns einige der grundlegenden Funktionsattribute genauer an. Diese Attribute können uns wichtige Informationen über die Funktion geben. Führen Sie den folgenden Code in der interaktiven Python-Shell aus:

```python
print(add.__name__)
print(add.__module__)
print(add.__doc__)
```

Wenn Sie diesen Code ausführen, sehen Sie die folgende Ausgabe:

```
add
__main__
Adds two things
```

Lassen Sie uns verstehen, was jedes dieser Attribute bedeutet:

- `__name__`: Dieses Attribut gibt uns den Namen der Funktion. In unserem Fall heißt die Funktion `add`.
- `__module__`: Es sagt uns, in welchem Modul die Funktion definiert ist. Wenn wir Code in der interaktiven Shell ausführen, ist das Modul normalerweise `__main__`.
- `__doc__`: Dies ist die Dokumentationszeichenkette (Docstring) der Funktion. Sie bietet eine kurze Beschreibung dessen, was die Funktion tut.

## Untersuchung des Funktionscodes

Das `__code__`-Attribut einer Funktion ist sehr interessant. Es enthält Informationen darüber, wie die Funktion implementiert ist, einschließlich ihres Bytecodes und anderer Details. Lassen Sie uns sehen, was wir daraus lernen können. Führen Sie den folgenden Code in der interaktiven Python-Shell aus:

```python
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)
```

Die Ausgabe wird sein:

```
('x', 'y')
2
```

Hier ist, was diese Attribute uns sagen:

- `co_varnames`: Es ist ein Tupel, das die Namen aller lokalen Variablen enthält, die von der Funktion verwendet werden. In unserer `add`-Funktion sind die lokalen Variablen `x` und `y`.
- `co_argcount`: Dieses Attribut sagt uns, wie viele Argumente die Funktion erwartet. Unsere `add`-Funktion erwartet zwei Argumente, also ist der Wert 2.

Wenn Sie neugierig sind und mehr Attribute des `__code__`-Objekts untersuchen möchten, können Sie die `dir()`-Funktion erneut verwenden. Führen Sie den folgenden Code aus:

```python
dir(add.__code__)
```

Dies wird alle Attribute des Code-Objekts anzeigen, die tiefergehende Details darüber enthalten, wie die Funktion implementiert ist.
