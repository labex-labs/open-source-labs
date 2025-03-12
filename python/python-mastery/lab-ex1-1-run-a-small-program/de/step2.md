# Erstellen eines einfachen Python-Programms

Nachdem wir bestätigt haben, dass Python korrekt funktioniert, ist es an der Zeit, unsere erste Python-Programmdatei zu erstellen. Für Anfänger ist es immer eine gute Idee, mit etwas Einfachem zu beginnen, bevor Sie zu komplexeren Programmen übergehen. Auf diese Weise können Sie die grundlegenden Konzepte und die Syntax von Python schrittweise verstehen.

## Erstellen Ihrer ersten Python-Datei

Zunächst erstellen wir eine neue Python-Datei. So können Sie es machen:

1. Im WebIDE wird Ihnen ein Panel auf der linken Seite des Bildschirms auffallen, das als Explorer-Panel bezeichnet wird. Dieses Panel hilft Ihnen, sich durch verschiedene Dateien und Verzeichnisse in Ihrem Projekt zu bewegen. Finden Sie dieses Panel.

2. Sobald Sie das Explorer-Panel gefunden haben, müssen Sie zum Verzeichnis `/home/labex/project` navigieren. Hier werden wir unser Python-Programm speichern.

3. Klicken Sie mit der rechten Maustaste irgendwo im Explorer-Panel. Ein Menü wird erscheinen. Wählen Sie aus diesem Menü "New File" (Neue Datei) aus. Diese Aktion erstellt eine neue, leere Datei.

4. Nachdem Sie die neue Datei erstellt haben, müssen Sie ihr einen Namen geben. Benennen Sie die Datei `hello.py`. In Python haben Dateien normalerweise die Endung `.py`, was darauf hinweist, dass sie Python-Code enthalten.

5. Öffnen Sie jetzt die neu erstellte `hello.py`-Datei im Editor. Geben Sie im Editor den folgenden Code ein:

   ```python
   # This is a simple Python program

   name = input("Enter your name: ")
   print(f"Hello, {name}! Welcome to Python programming.")
   ```

   Lassen Sie uns diesen Code analysieren. Die Zeile, die mit `#` beginnt, ist ein Kommentar. Kommentare werden verwendet, um zu erklären, was der Code tut, und werden vom Python-Interpreter ignoriert. Die `input()`-Funktion wird verwendet, um Benutzereingaben zu erhalten. Sie zeigt die Nachricht "Enter your name: " an und wartet darauf, dass der Benutzer etwas eingibt. Der vom Benutzer eingegebene Wert wird dann in der Variable `name` gespeichert. Die `print()`-Funktion wird verwendet, um Ausgaben auf dem Bildschirm anzuzeigen. Das `f"Hello, {name}!"` ist ein f-String, was eine bequeme Möglichkeit ist, Strings in Python zu formatieren. Es ermöglicht Ihnen, den Wert einer Variable direkt in einen String einzufügen.

6. Nachdem Sie den Code eingegeben haben, müssen Sie die Datei speichern. Sie können dies tun, indem Sie auf Ihrer Tastatur Ctrl+S drücken oder indem Sie aus dem Menü "File > Save" (Datei > Speichern) auswählen. Das Speichern der Datei stellt sicher, dass Ihre Änderungen beibehalten werden.

## Ausführen Ihres ersten Python-Programms

Nachdem Sie Ihr Python-Programm erstellt und gespeichert haben, ist es an der Zeit, es auszuführen. So geht es:

1. Öffnen Sie ein Terminal im WebIDE, wenn es noch nicht geöffnet ist. Das Terminal ermöglicht es Ihnen, Befehle auszuführen und Programme auszuführen.

2. Bevor Sie das Python-Programm ausführen, müssen Sie sicherstellen, dass Sie sich im richtigen Verzeichnis befinden. Geben Sie den folgenden Befehl im Terminal ein:

   ```bash
   cd ~/project
   ```

   Dieser Befehl wechselt das aktuelle Arbeitsverzeichnis in das `project`-Verzeichnis in Ihrem Home-Verzeichnis.

3. Sobald Sie sich im richtigen Verzeichnis befinden, können Sie Ihr Python-Programm ausführen. Geben Sie den folgenden Befehl im Terminal ein:

   ```bash
   python3 hello.py
   ```

   Dieser Befehl teilt dem Python-Interpreter mit, die `hello.py`-Datei auszuführen.

4. Wenn das Programm ausgeführt wird, werden Sie aufgefordert, Ihren Namen einzugeben. Geben Sie Ihren Namen ein und drücken Sie die Eingabetaste.

5. Nachdem Sie die Eingabetaste gedrückt haben, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

   ```
   Enter your name: John
   Hello, John! Welcome to Python programming.
   ```

   Die tatsächliche Ausgabe wird den Namen anzeigen, den Sie eingegeben haben, anstelle von "John".

Dieses einfache Programm demonstriert mehrere wichtige Konzepte in Python:

- Erstellen einer Python-Datei: Sie haben gelernt, wie Sie eine neue Python-Datei im WebIDE erstellen.
- Hinzufügen von Kommentaren: Kommentare werden verwendet, um den Code zu erklären und ihn verständlicher zu machen.
- Erhalten von Benutzereingaben mit der `input()`-Funktion: Diese Funktion ermöglicht es Ihrem Programm, mit dem Benutzer zu interagieren.
- Verwenden von Variablen zum Speichern von Daten: Variablen werden verwendet, um Werte zu speichern, die später im Programm verwendet werden können.
- Anzeigen von Ausgaben mit der `print()`-Funktion: Diese Funktion wird verwendet, um Informationen auf dem Bildschirm anzuzeigen.
- Verwenden von f-Strings zur String-Formatierung: F-Strings bieten eine bequeme Möglichkeit, Variablen in Strings einzufügen.
