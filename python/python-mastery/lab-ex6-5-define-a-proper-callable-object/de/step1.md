# Verständnis von Validator-Klassen

In diesem Lab werden wir auf einer Reihe von Validator-Klassen aufbauen, um ein aufrufbares Objekt zu erstellen. Bevor wir mit dem Bau beginnen, ist es wichtig, die in der Datei `validate.py` bereitgestellten Validator-Klassen zu verstehen. Diese Klassen helfen uns bei der Typüberprüfung, was ein entscheidender Bestandteil dafür ist, dass unser Code wie erwartet funktioniert.

Lassen Sie uns beginnen, indem Sie die Datei `validate.py` in der WebIDE öffnen. Diese Datei enthält den Code für die Validator-Klassen, die wir verwenden werden. Um sie zu öffnen, führen Sie den folgenden Befehl im Terminal aus:

```bash
code /home/labex/project/validate.py
```

Sobald Sie die Datei geöffnet haben, werden Sie feststellen, dass sie mehrere Klassen enthält. Hier ist eine kurze Übersicht darüber, was jede Klasse macht:

1. `Validator`: Dies ist eine Basisklasse. Sie hat eine Methode `check`, die derzeit jedoch nichts tut. Sie dient als Ausgangspunkt für die anderen Validator-Klassen.
2. `Typed`: Dies ist eine Unterklasse von `Validator`. Ihre Hauptaufgabe besteht darin, zu überprüfen, ob ein Wert einen bestimmten Typ hat.
3. `Integer`, `Float` und `String`: Dies sind spezifische Typ-Validatoren, die von `Typed` erben. Sie sind darauf ausgelegt, zu überprüfen, ob ein Wert eine Ganzzahl, eine Fließkommazahl oder eine Zeichenkette ist.

Jetzt sehen wir uns an, wie diese Validator-Klassen in der Praxis funktionieren. Wir werden eine neue Datei namens `test.py` erstellen, um sie zu testen. Um diese Datei zu erstellen und zu öffnen, führen Sie den folgenden Befehl aus:

```bash
code /home/labex/project/test.py
```

Sobald die Datei `test.py` geöffnet ist, fügen Sie den folgenden Code hinzu. Dieser Code wird die `Integer`- und `String`-Validatoren testen:

```python
from validate import Integer, String, Float

# Test Integer validator
print("Testing Integer validator:")
try:
    Integer.check(42)
    print("✓ Integer check passed for 42")
except TypeError as e:
    print(f"✗ Error: {e}")

try:
    Integer.check("Hello")
    print("✗ Integer check incorrectly passed for 'Hello'")
except TypeError as e:
    print(f"✓ Correctly raised error: {e}")

# Test String validator
print("\nTesting String validator:")
try:
    String.check("Hello")
    print("✓ String check passed for 'Hello'")
except TypeError as e:
    print(f"✗ Error: {e}")
```

In diesem Code importieren wir zunächst die `Integer`-, `String`- und `Float`-Validatoren aus der Datei `validate.py`. Dann testen wir den `Integer`-Validator, indem wir versuchen, einen ganzzahligen Wert (`42`) und einen Zeichenkettenwert (`"Hello"`) zu überprüfen. Wenn die Überprüfung für die Ganzzahl erfolgreich ist, geben wir eine Erfolgsmeldung aus. Wenn die Überprüfung für die Zeichenkette fehlerhaft erfolgreich ist, geben wir eine Fehlermeldung aus. Wenn die Überprüfung für die Zeichenkette korrekt einen `TypeError` auslöst, geben wir eine Erfolgsmeldung aus. Wir führen einen ähnlichen Test für den `String`-Validator durch.

Nachdem Sie den Code hinzugefügt haben, führen Sie die Testdatei mit dem folgenden Befehl aus:

```bash
python3 /home/labex/project/test.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Testing Integer validator:
✓ Integer check passed for 42
✓ Correctly raised error: Expected <class 'int'>

Testing String validator:
✓ String check passed for 'Hello'
```

Wie Sie sehen können, ermöglichen uns diese Validator-Klassen, die Typüberprüfung einfach durchzuführen. Beispielsweise wird beim Aufruf von `Integer.check(x)` ein `TypeError` ausgelöst, wenn `x` keine Ganzzahl ist.

Jetzt denken wir über ein praktisches Szenario nach. Angenommen, wir haben eine Funktion, die erfordert, dass ihre Argumente bestimmte Typen haben. Hier ist ein Beispiel für eine solche Funktion:

```python
def add(x, y):
    Integer.check(x)  # Make sure x is an integer
    Integer.check(y)  # Make sure y is an integer
    return x + y
```

Diese Funktion funktioniert, aber es gibt ein Problem. Wir müssen die Validator-Überprüfungen manuell hinzufügen, jedes Mal wenn wir die Typüberprüfung verwenden möchten. Dies kann zeitaufwendig und fehleranfällig sein, insbesondere bei größeren Funktionen oder Projekten.

In den nächsten Schritten werden wir dieses Problem lösen, indem wir ein aufrufbares Objekt erstellen. Dieses Objekt kann diese Typüberprüfungen automatisch basierend auf Funktionsannotationen anwenden. Auf diese Weise müssen wir die Überprüfungen nicht jedes Mal manuell hinzufügen.
