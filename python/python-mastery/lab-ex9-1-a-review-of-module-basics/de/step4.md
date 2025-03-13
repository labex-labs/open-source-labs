# Verwendung der `from module import`-Syntax

In Python gibt es verschiedene Möglichkeiten, Komponenten aus Modulen zu importieren. Eine dieser Möglichkeiten ist die `from module import`-Syntax, die wir in diesem Abschnitt untersuchen werden.

Wenn Sie Komponenten aus einem Modul importieren, ist es oft eine gute Idee, mit einem sauberen Arbeitsbereich zu beginnen. Dies stellt sicher, dass es keine verbleibenden Variablen oder Einstellungen aus früheren Interaktionen gibt, die unseren aktuellen Versuch stören könnten.

1. Starten Sie den Python-Interpreter neu, um einen sauberen Zustand zu erhalten:

```python
>>> exit()
```

Dieser Befehl beendet die aktuelle Python-Interpreter-Sitzung. Nach dem Beenden starten wir eine neue Sitzung, um eine frische Umgebung sicherzustellen.

```bash
python3
```

Dieser Bash-Befehl startet eine neue Python 3-Interpreter-Sitzung. Jetzt, da wir eine saubere Python-Umgebung haben, können wir beginnen, Komponenten aus einem Modul zu importieren.

2. Importieren Sie spezifische Komponenten aus einem Modul mit der `from module import`-Syntax:

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

Hier verwenden wir die Anweisung `from simplemod import foo`, um nur die Funktion `foo` aus dem `simplemod`-Modul zu importieren. Beachten Sie, dass obwohl wir nur die Funktion `foo` angefordert haben, das gesamte `simplemod`-Modul geladen wurde. Dies wird durch die Ausgabe "Loaded simplemod" angezeigt. Der Grund dafür ist, dass Python das gesamte Modul laden muss, um auf die Funktion `foo` zugreifen zu können.

3. Wenn Sie `from module import` verwenden, können Sie nicht auf das Modul selbst zugreifen:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

Wenn wir die `from module import`-Syntax verwenden, bringen wir nur die angegebenen Komponenten direkt in unseren Namensraum ein. Der Modulname selbst wird nicht importiert. Wenn wir also versuchen, auf `simplemod.foo()` zuzugreifen, erkennt Python `simplemod` nicht, weil es nicht auf diese Weise importiert wurde.

4. Sie können mehrere Komponenten auf einmal importieren:

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

Die `from module import`-Syntax ermöglicht es uns, mehrere Komponenten aus einem Modul in einer einzigen Anweisung zu importieren. Hier importieren wir sowohl die Variable `x` als auch die Funktion `foo` aus dem `simplemod`-Modul. Nach dem Import können wir direkt auf diese Komponenten in unserem Code zugreifen.

5. Wenn Sie eine Variable aus einem Modul importieren, erstellen Sie eine neue Referenz auf das Objekt, nicht einen Link zur Variable im Modul:

```python
>>> x = 13  # Ändern Sie die lokale Variable x
>>> x
13
>>> foo()
x is 42  # Die Funktion verwendet immer noch die Variable x des Moduls, nicht Ihre lokale Variable x
```

Wenn wir eine Variable aus einem Modul importieren, erstellen wir im Wesentlichen eine neue Referenz auf dasselbe Objekt in unserem lokalen Namensraum. Wenn wir also die lokale Variable `x` auf `13` ändern, wirkt sich dies nicht auf die Variable `x` im `simplemod`-Modul aus. Die Funktion `foo()` bezieht sich immer noch auf die Variable `x` des Moduls, die `42` ist. Das Verständnis dieses Konzepts ist entscheidend, um Verwirrungen in Ihrem Code zu vermeiden.
