# Erstellen eines einfachen Moduls

Beginnen wir unsere Reise in die Welt der Python-Module, indem wir ein einfaches Modul erstellen. In Python ist ein Modul im Wesentlichen eine Datei mit der Endung `.py`, die Python-Code enthält. Stellen Sie sich es als einen Behälter vor, in dem Sie verwandte Funktionen, Klassen und Variablen zusammenfassen können. Dies macht Ihren Code besser organisiert und leichter zu verwalten, insbesondere wenn Ihre Projekte an Größe zunehmen.

1. Öffnen Sie zunächst die WebIDE. Sobald sie geöffnet ist, müssen Sie eine neue Datei erstellen. Um dies zu tun, klicken Sie auf "File" in der Menüleiste und wählen Sie dann "New File". Benennen Sie diese neue Datei `simplemod.py` und speichern Sie sie im Verzeichnis `/home/labex/project`. In diesem Verzeichnis werden wir alle Dateien für dieses Experiment aufbewahren.

2. Fügen wir nun etwas Code in unsere neu erstellte Datei `simplemod.py` ein. Der folgende Code definiert einige grundlegende Elemente, die Sie üblicherweise in einem Python-Modul finden.

```python
# simplemod.py

x = 42        # A global variable

# A simple function
def foo():
    print('x is', x)

# A simple class
class Spam:
    def yow(self):
        print('Yow!')

# A scripting statement
print('Loaded simplemod')
```

In diesem Code:

- `x = 42` erstellt eine globale Variable namens `x` und weist ihr den Wert `42` zu. Globale Variablen können von überall innerhalb des Moduls aus zugegriffen werden.
- Die Funktion `foo()` ist so definiert, dass sie den Wert der globalen Variable `x` ausgibt. Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe ausführen.
- Die Klasse `Spam` ist ein Bauplan für das Erstellen von Objekten. Sie hat eine Methode namens `yow()`, die einfach die Zeichenkette 'Yow!' ausgibt. Methoden sind Funktionen, die zu einer Klasse gehören.
- Die Anweisung `print('Loaded simplemod')` ist eine Skriptanweisung. Sie wird ausgeführt, sobald das Modul geladen wird, was uns hilft, zu bestätigen, dass das Modul erfolgreich geladen wurde.

3. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei. Sie können dies tun, indem Sie `Strg+S` auf Ihrer Tastatur drücken oder indem Sie "File" > "Save" aus dem Menü auswählen. Das Speichern der Datei stellt sicher, dass alle Änderungen, die Sie vorgenommen haben, beibehalten werden.

Schauen wir uns genauer an, was dieses Modul enthält:

- Eine globale Variable `x` mit dem Wert `42`. Diese Variable kann im gesamten Modul verwendet werden und sogar von anderen Modulen aus zugegriffen werden, wenn sie korrekt importiert wird.
- Eine Funktion `foo()`, die den Wert von `x` ausgibt. Funktionen sind nützlich, um wiederholende Aufgaben auszuführen, ohne den gleichen Code mehrmals schreiben zu müssen.
- Eine Klasse `Spam` mit einer Methode `yow()`. Klassen und Methoden sind grundlegende Konzepte der objektorientierten Programmierung, die es Ihnen ermöglichen, komplexe Datenstrukturen und Verhaltensweisen zu erstellen.
- Eine `print`-Anweisung, die ausgeführt wird, wenn das Modul geladen wird. Diese Anweisung dient als visueller Indikator dafür, dass das Modul erfolgreich in die Python-Umgebung geladen wurde.

Die `print`-Anweisung am Ende wird uns helfen, zu beobachten, wann das Modul geladen wird, was wichtig für das Debugging und das Verständnis der Funktionsweise von Modulen in Python ist.
