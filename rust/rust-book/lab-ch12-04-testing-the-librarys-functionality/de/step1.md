# Test-getriebene Entwicklung

Jetzt, da wir die Logik in `src/lib.rs` extrahiert haben und die Argumenteinsammlung und die Fehlerbehandlung in `src/main.rs` belassen haben, ist es viel einfacher, Tests für die Kernfunktionalität unseres Codes zu schreiben. Wir können Funktionen direkt mit verschiedenen Argumenten aufrufen und Rückgabewerte überprüfen, ohne dass wir unser Binärprogramm von der Befehlszeile aufrufen müssen.

In diesem Abschnitt fügen wir die Suchlogik zum `minigrep`-Programm hinzu, indem wir den Prozess der test-getriebenen Entwicklung (TDD) mit den folgenden Schritten anwenden:

1.  Schreiben Sie einen Test, der fehlschlägt, und führen Sie ihn aus, um sicherzustellen, dass er aus dem erwarteten Grund fehlschlägt.
2.  Schreiben Sie oder ändern Sie nur so viel Code, dass der neue Test erfolgreich ist.
3.  Optimieren Sie den gerade hinzugefügten oder geänderten Code und stellen Sie sicher, dass die Tests weiterhin erfolgreich sind.
4.  Wiederholen Sie ab Schritt 1!

Obwohl es nur eine von vielen Möglichkeiten ist, Software zu schreiben, kann die TDD die Codegestaltung unterstützen. Das Schreiben des Tests bevor Sie den Code schreiben, der den Test erfolgreich macht, hilft, eine hohe Testabdeckung während des gesamten Prozesses aufrechtzuerhalten.

Wir werden die Implementierung der Funktionalität test-getrieben entwickeln, die tatsächlich das Suchen nach der Abfragezeichenfolge in den Dateiinhalten durchführt und eine Liste von Zeilen erzeugt, die mit der Abfrage übereinstimmen. Wir werden diese Funktionalität in einer Funktion namens `search` hinzufügen.
