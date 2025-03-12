# Erstellen eines fortgeschritteneren Python-Programms

Nachdem Sie die Grundlagen von Python erlernt haben, ist es an der Zeit, den nächsten Schritt zu gehen und ein fortgeschritteneres Python-Programm zu erstellen. Dieses Programm wird ASCII-Art-Muster generieren, die einfache, aber optisch interessante Designs aus Textzeichen sind. Durch die Arbeit an diesem Programm werden Sie mehrere wichtige Python-Konzepte lernen und anwenden, wie das Importieren von Modulen, das Definieren von Funktionen und die Verarbeitung von Befehlszeilenargumenten.

## Erstellen des ASCII-Art-Programms

1. Zunächst müssen wir die Datei `art.py` im WebIDE öffnen. Diese Datei wurde während des Einrichtungsprozesses erstellt. Sie finden sie im Verzeichnis `/home/labex/project`. Das Öffnen dieser Datei ist der Ausgangspunkt für das Schreiben unseres ASCII-Art-Programms.

2. Sobald die Datei geöffnet ist, werden Sie feststellen, dass sie möglicherweise bereits etwas Inhalt hat. Wir müssen diesen löschen, da wir unseren eigenen Code von Grund auf neu schreiben werden. Löschen Sie also alle vorhandenen Inhalte in der Datei. Kopieren Sie dann den folgenden Code in die Datei `art.py`. Dieser Code ist der Kern unseres ASCII-Art-Generators.

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. Nachdem Sie den Code in die Datei kopiert haben, ist es wichtig, Ihre Arbeit zu speichern. Sie können dies tun, indem Sie auf Ihrer Tastatur Ctrl + S drücken. Alternativ können Sie zum Menü gehen und "File > Save" auswählen. Das Speichern der Datei stellt sicher, dass Ihr Code gespeichert und zum Ausführen bereit ist.

## Verständnis des Codes

Schauen wir uns genauer an, was dieses Programm tut. Das Verständnis des Codes ist entscheidend, damit Sie ihn in Zukunft modifizieren und erweitern können.

- **Import-Anweisungen**: Die Zeilen `import sys` und `import random` werden verwendet, um Python's integrierte Module einzubinden. Das `sys`-Modul bietet Zugang zu einigen Variablen, die vom Python-Interpreter verwendet oder verwaltet werden, sowie zu Funktionen, die stark mit dem Interpreter interagieren. Das `random`-Modul ermöglicht es uns, Zufallszahlen zu generieren, die wir verwenden werden, um zufällige ASCII-Art-Muster zu erstellen.
- **Zeichensatz**: Die Zeile `chars = '\|/'` definiert den Zeichensatz, der für die Erstellung unseres ASCII-Art verwendet wird. Diese Zeichen werden zufällig ausgewählt, um die Muster zu bilden.
- **Die `draw()`-Funktion**: Diese Funktion ist für die Erstellung der ASCII-Art-Muster verantwortlich. Sie nimmt zwei Argumente, `rows` und `columns`, die die Abmessungen des Musters angeben. Innerhalb der Funktion wird eine Schleife verwendet, um jede Zeile des Musters zu erstellen, indem Zeichen aus dem `chars`-Zeichensatz zufällig ausgewählt werden.
- **Hauptblock**: Der Block `if __name__ == '__main__':` ist ein spezielles Konstrukt in Python. Es stellt sicher, dass der Code innerhalb dieses Blocks nur ausgeführt wird, wenn die Datei `art.py` direkt ausgeführt wird. Wenn die Datei in eine andere Python-Datei importiert wird, wird dieser Code nicht ausgeführt.
- **Argumentverarbeitung**: Die Variable `sys.argv` enthält die Befehlszeilenargumente, die an das Programm übergeben werden. Wir überprüfen, ob genau 3 Argumente angegeben werden (der Name des Skripts selbst plus zwei Zahlen, die die Anzahl der Zeilen und Spalten darstellen). Dies hilft uns sicherzustellen, dass der Benutzer die richtigen Eingaben macht.
- **Fehlerbehandlung**: Der `try/except`-Block wird verwendet, um Fehler zu erkennen, die auftreten können. Wenn der Benutzer ungültige Eingaben macht, wie z. B. nicht ganzzahlige Werte für die Zeilen und Spalten, wird der `try`-Block einen `ValueError` auslösen, und der `except`-Block wird eine Fehlermeldung ausgeben und das Programm beenden.

## Ausführen des Programms

1. Um unser Programm auszuführen, müssen wir zunächst ein Terminal im WebIDE öffnen. Im Terminal geben wir die Befehle ein, um unser Python-Skript auszuführen.

2. Sobald das Terminal geöffnet ist, müssen wir in das Projektverzeichnis navigieren. Hier befindet sich unsere Datei `art.py`. Verwenden Sie den folgenden Befehl im Terminal:

   ```bash
   cd ~/project
   ```

   Dieser Befehl wechselt das aktuelle Arbeitsverzeichnis in das Projektverzeichnis.

3. Nun, da wir uns im richtigen Verzeichnis befinden, können wir das Programm ausführen. Verwenden Sie den folgenden Befehl:

   ```bash
   python3 art.py 5 10
   ```

   Dieser Befehl teilt Python mit, das Skript `art.py` mit 5 Zeilen und 10 Spalten auszuführen. Wenn Sie diesen Befehl ausführen, sehen Sie ein 5×10-Muster von Zeichen im Terminal. Die Ausgabe sieht in etwa so aus:

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   Denken Sie daran, dass das tatsächliche Muster zufällig ist, sodass Ihre Ausgabe sich von dem hier gezeigten Beispiel unterscheiden wird.

4. Sie können mit verschiedenen Abmessungen experimentieren, indem Sie die Argumente im Befehl ändern. Versuchen Sie beispielsweise den folgenden Befehl:

   ```bash
   python3 art.py 8 15
   ```

   Dies wird ein größeres Muster mit 8 Zeilen und 15 Spalten generieren.

5. Um die Fehlerbehandlung in Aktion zu sehen, versuchen Sie, ungültige Argumente anzugeben. Führen Sie den folgenden Befehl aus:

   ```bash
   python3 art.py
   ```

   Sie sollten eine Fehlermeldung wie die folgende sehen:

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## Experimentieren mit dem Code

Sie können die ASCII-Art-Muster interessanter gestalten, indem Sie den Zeichensatz ändern. So können Sie es machen:

1. Öffnen Sie die Datei `art.py` erneut im Editor. Hier werden wir die Änderungen am Code vornehmen.

2. Suchen Sie die Variable `chars` im Code. Ändern Sie sie, um andere Zeichen zu verwenden. Beispielsweise können Sie den folgenden Code verwenden:

   ```python
   chars = '*#@+.'
   ```

   Dies wird den Zeichensatz ändern, der für die Erstellung des ASCII-Art verwendet wird.

3. Nachdem Sie die Änderung vorgenommen haben, speichern Sie die Datei erneut mit Ctrl + S oder "File > Save". Führen Sie dann das Programm mit dem folgenden Befehl aus:

   ```bash
   python3 art.py 5 10
   ```

   Jetzt sehen Sie ein anderes Muster mit Ihren neuen Zeichen.

Diese Übung demonstriert mehrere wichtige Python-Konzepte, darunter:

- Modulimporte: Wie man zusätzliche Funktionen aus Python's integrierten Modulen einbindet.
- Funktionsdefinition: Wie man Funktionen definiert und verwendet, um seinen Code zu organisieren.
- Befehlszeilenargumentverarbeitung: Wie man Benutzereingaben von der Befehlszeile akzeptiert und verarbeitet.
- Fehlerbehandlung mit try/except: Wie man Fehler in seinem Programm elegant behandelt.
- Zeichenkettenmanipulation: Wie man Zeichenketten erstellt und manipuliert, um die ASCII-Art-Muster zu bilden.
- Zufallszahlengenerierung: Wie man Zufallswerte generiert, um einzigartige Muster zu erstellen.
- Listen-Abstraktionen: Eine kompakte Möglichkeit, Listen in Python zu erstellen, die in der `draw()`-Funktion verwendet wird.
