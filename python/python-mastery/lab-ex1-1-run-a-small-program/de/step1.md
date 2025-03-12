# Überprüfen der Python-Installation und Verwenden des interaktiven Interpreters

Der interaktive Python-Interpreter ist ein sehr nützliches Werkzeug. Es ermöglicht Ihnen, Python-Code Zeile für Zeile auszuführen und sofort die Ergebnisse zu sehen. Dies ist ideal für Anfänger, da Sie kleine Code-Schnipsel testen können, ohne ein ganzes Programm schreiben zu müssen. Bevor wir mit der Schreibung vollwertiger Programme beginnen, müssen wir sicherstellen, dass Python korrekt auf Ihrem System installiert ist. Anschließend lernen wir, wie Sie diesen Interpreter verwenden, um Python-Code auszuführen.

## Starten des Python-Interpreters

1. Zunächst müssen Sie im WebIDE ein Terminal öffnen. Das Terminal ist wie ein Befehlszentrum, in dem Sie Befehle eingeben können, um mit Ihrem Computer zu interagieren. Sie finden eine Terminal-Tab am unteren Bildschirmrand. Sobald Sie sie geöffnet haben, können Sie mit der Eingabe von Befehlen beginnen.

2. Im Terminal werden wir überprüfen, ob Python installiert ist und welche Version Sie haben. Geben Sie den folgenden Befehl ein und drücken Sie dann die Eingabetaste:

   ```bash
   python3 --version
   ```

   Dieser Befehl fordert Ihr System auf, die Version von Python anzuzeigen, die derzeit installiert ist. Wenn Python korrekt installiert ist, sehen Sie eine Ausgabe ähnlich der folgenden:

   ```
   Python 3.10.x
   ```

   Das `x` hier repräsentiert eine spezifische Patch-Nummer, die je nach Ihrer Installation variieren kann.

3. Da wir nun wissen, dass Python installiert ist, lassen Sie uns den interaktiven Python-Interpreter starten. Geben Sie den folgenden Befehl im Terminal ein und drücken Sie die Eingabetaste:

   ```bash
   python3
   ```

   Nachdem Sie die Eingabetaste gedrückt haben, sehen Sie einige Informationen über die Python-Version und andere Details. Die Ausgabe sieht in etwa so aus:

   ```
   Python 3.10.x (default, ...)
   [GCC x.x.x] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   Die `>>>`-Eingabeaufforderung signalisiert, dass der Python-Interpreter gestartet und läuft und darauf wartet, dass Sie Python-Befehle eingeben.

## Versuchen einfacher Python-Befehle

Da der Python-Interpreter jetzt läuft, lassen Sie uns einige grundlegende Python-Befehle ausprobieren. Diese Befehle helfen Ihnen zu verstehen, wie Python funktioniert und wie Sie den Interpreter verwenden.

1. Geben Sie an der `>>>`-Eingabeaufforderung den folgenden Befehl ein und drücken Sie die Eingabetaste:

   ```python
   >>> print('Hello World')
   ```

   Die `print`-Funktion in Python wird verwendet, um Text auf dem Bildschirm anzuzeigen. Wenn Sie diesen Befehl ausführen, sehen Sie die folgende Ausgabe:

   ```
   Hello World
   >>>
   ```

   Dies zeigt, dass die `print`-Funktion den Text 'Hello World' erfolgreich angezeigt hat.

2. Versuchen wir eine einfache mathematische Berechnung. Geben Sie an der Eingabeaufforderung ein:

   ```python
   >>> 2 + 3
   ```

   Python wertet diesen Ausdruck automatisch aus und zeigt Ihnen das Ergebnis. Sie sehen:

   ```
   5
   >>>
   ```

   Dies zeigt, dass Python grundlegende arithmetische Operationen ausführen kann.

3. Als Nächstes erstellen wir eine Variable und verwenden sie. Variablen in Python werden verwendet, um Daten zu speichern. Geben Sie die folgenden Befehle an der Eingabeaufforderung ein:

   ```python
   >>> message = "Learning Python"
   >>> print(message)
   ```

   In der ersten Zeile erstellen wir eine Variable namens `message` und speichern die Zeichenkette "Learning Python" darin. In der zweiten Zeile verwenden wir die `print`-Funktion, um den in der `message`-Variable gespeicherten Wert anzuzeigen. Die Ausgabe wird sein:

   ```
   Learning Python
   >>>
   ```

   Der Python-Interpreter führt jede Code-Zeile aus, sobald Sie sie eingegeben haben. Dies macht es zu einem großartigen Werkzeug, um Ideen schnell zu testen und Python-Konzepte zu lernen.

## Beenden des Interpreters

Wenn Sie mit dem Experimentieren mit dem Python-Interpreter fertig sind, können Sie ihn auf eine der folgenden Arten beenden:

1. Sie können den folgenden Befehl an der `>>>`-Eingabeaufforderung eingeben und die Eingabetaste drücken:

   ```python
   >>> exit()
   ```

   Oder Sie können diesen alternativen Befehl verwenden:

   ```python
   >>> quit()
   ```

   Beide Befehle veranlassen den Python-Interpreter, das Ausführen zu beenden und Sie zurück zum normalen Terminal-Prompt zu bringen.

2. Eine andere Möglichkeit, den Interpreter zu beenden, ist, die Tasten Ctrl+D auf Ihrer Tastatur zu drücken. Dies ist eine Tastenkombination, die ebenfalls den Python-Interpreter stoppt.

Nachdem Sie den Interpreter beendet haben, kehren Sie zum normalen Terminal-Prompt zurück, wo Sie andere Befehle auf Ihrem System ausführen können.
