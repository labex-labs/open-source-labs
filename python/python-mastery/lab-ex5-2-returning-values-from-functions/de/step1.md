# Rückgabe mehrerer Werte aus Funktionen

In Python gibt es eine praktische Lösung, wenn Sie möchten, dass eine Funktion mehr als einen Wert zurückgibt: die Rückgabe eines Tupels. Ein Tupel ist eine Art von Datenstruktur in Python. Es ist eine unveränderliche Sequenz, was bedeutet, dass Sie die Elemente eines Tupels nicht ändern können, sobald es erstellt wurde. Tupel sind nützlich, da sie mehrere Werte unterschiedlicher Typen an einem Ort speichern können.

Erstellen wir nun eine Funktion, um Konfigurationszeilen im Format `name=value` zu analysieren. Das Ziel dieser Funktion besteht darin, eine Zeile in diesem Format zu nehmen und sowohl den Namen als auch den Wert als separate Elemente zurückzugeben.

1. Zunächst müssen Sie eine neue Python-Datei erstellen. In dieser Datei werden der Code für unsere Funktion und der Testcode gespeichert. Erstellen Sie im Projektverzeichnis eine Datei mit dem Namen `return_values.py`. Sie können den folgenden Befehl im Terminal ausführen, um diese Datei zu erstellen:

```
touch ~/project/return_values.py
```

2. Öffnen Sie nun die Datei `return_values.py` in Ihrem Code-Editor. In dieser Datei schreiben wir die Funktion `parse_line`. Diese Funktion nimmt eine Zeile als Eingabe, teilt sie am ersten '='-Zeichen auf und gibt den Namen und den Wert als Tupel zurück.

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple: A tuple containing (name, value)
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
```

In dieser Funktion wird die Methode `split` verwendet, um die Eingabezeile am ersten '='-Zeichen in zwei Teile zu teilen. Wenn die Zeile im richtigen `name=value`-Format vorliegt, extrahieren wir den Namen und den Wert und geben sie als Tupel zurück.

3. Nachdem die Funktion definiert wurde, müssen wir einige Testcode hinzufügen, um zu überprüfen, ob die Funktion wie erwartet funktioniert. Der Testcode ruft die Funktion `parse_line` mit einer Beispiel-Eingabe auf und gibt die Ergebnisse aus.

```python
# Test the parse_line function
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Unpacking the tuple into separate variables
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

Im Testcode rufen wir zunächst die Funktion `parse_line` auf und speichern das zurückgegebene Tupel in der Variablen `result`. Dann geben wir dieses Tupel aus. Anschließend verwenden wir die Tupel-Auf unpacking, um die Elemente des Tupels direkt den Variablen `name` und `value` zuzuweisen und sie getrennt auszugeben.

4. Nachdem Sie die Funktion und den Testcode geschrieben haben, speichern Sie die Datei `return_values.py`. Öffnen Sie dann das Terminal und führen Sie den folgenden Befehl aus, um das Python-Skript auszuführen:

```
python ~/project/return_values.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**Erklärung:**

- Die Funktion `parse_line` teilt die Eingabezeichenfolge am '='-Zeichen mithilfe der Methode `split` auf. Diese Methode teilt die Zeichenfolge in Teile auf, basierend auf dem angegebenen Trennzeichen.
- Sie gibt beide Teile als Tupel zurück, indem sie die Syntax `return (name, value)` verwendet. Ein Tupel ist eine Möglichkeit, mehrere Werte zusammenzufassen.
- Wenn Sie die Funktion aufrufen, haben Sie zwei Optionen. Sie können entweder das gesamte Tupel in einer Variablen speichern, wie wir es mit der Variablen `result` getan haben. Oder Sie können das Tupel direkt in separate Variablen "entpacken" (unpacking), indem Sie die Syntax `name, value = parse_line(...)` verwenden. Dies erleichtert die Arbeit mit den einzelnen Werten.

Dieses Muster der Rückgabe mehrerer Werte als Tupel ist in Python sehr verbreitet. Es macht Funktionen vielseitiger, da sie mehr als eine Information an den aufrufenden Code liefern können.
