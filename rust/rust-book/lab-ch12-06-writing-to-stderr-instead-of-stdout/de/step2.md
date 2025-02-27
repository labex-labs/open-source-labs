# Überprüfen, wo Fehler geschrieben werden

Zunächst beobachten wir, wie der von `minigrep` ausgegebene Inhalt derzeit an die Standardausgabe geschrieben wird, einschließlich aller Fehlermeldungen, die wir stattdessen an die Standardfehlerausgabe schreiben möchten. Wir werden das tun, indem wir den Standardausgabestream in eine Datei umleiten, während wir absichtlich einen Fehler verursachen. Wir werden den Standardfehlerstream nicht umleiten, sodass alle an die Standardfehlerausgabe gesendete Inhalte weiterhin auf dem Bildschirm angezeigt werden.

Es wird erwartet, dass Befehlszeilenprogramme Fehlermeldungen an den Standardfehlerstream senden, sodass wir Fehlermeldungen auch dann noch auf dem Bildschirm sehen können, wenn wir den Standardausgabestream in eine Datei umleiten. Unser Programm verhält sich derzeit nicht gut: wir werden sehen, dass es die Fehlermeldungsausgabe stattdessen in eine Datei speichert!

Um dieses Verhalten zu demonstrieren, führen wir das Programm mit `>` und dem Dateipfad, _output.txt_, zu dem wir den Standardausgabestream umleiten möchten. Wir übergeben keine Argumente, was einen Fehler verursachen sollte:

```bash
cargo run > output.txt
```

Die `>`-Syntax sagt der Shell, den Inhalt der Standardausgabe in _output.txt_ statt auf dem Bildschirm zu schreiben. Wir haben die erwartete Fehlermeldung nicht auf dem Bildschirm gesehen, was bedeutet, dass sie vermutlich in die Datei gekommen ist. Dies ist der Inhalt von _output.txt_:

```rust
Problem parsing arguments: not enough arguments
```

Ja, unsere Fehlermeldung wird an die Standardausgabe geschrieben. Es ist viel nützlicher, dass Fehlermeldungen wie diese an die Standardfehlerausgabe geschrieben werden, sodass nur Daten aus einem erfolgreichen Lauf in die Datei landen. Wir werden das ändern.
