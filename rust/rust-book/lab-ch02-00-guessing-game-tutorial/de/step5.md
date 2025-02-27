# Benutzer-Eingaben empfangen

Denken Sie daran, dass wir die Eingabe/Ausgabe-Funktionalität aus der Standardbibliothek mit `use std::io;` in der ersten Zeile des Programms eingeschlossen haben. Jetzt rufen wir die `stdin`-Funktion aus dem `io`-Modul auf, was uns ermöglicht, Benutzer-Eingaben zu verarbeiten:

```rust
io::stdin()
 .read_line(&mut guess)
```

Wenn wir die `io`-Bibliothek am Anfang des Programms nicht mit `use std::io;` importiert hätten, könnten wir die Funktion auch weiterhin verwenden, indem wir diesen Funktionsaufruf als `std::io::stdin` schreiben. Die `stdin`-Funktion gibt eine Instanz von `std::io::Stdin` zurück, die ein Typ ist, der einen Zugangspunkt für die Standardeingabe Ihres Terminals darstellt.

Als nächstes ruft die Zeile `.read_line(&mut guess)` die `read_line`-Methode auf dem Standardeingabe-Zugangspunkt auf, um Eingaben vom Benutzer zu erhalten. Wir übergeben auch `&mut guess` als Argument an `read_line`, um zu sagen, in welche Zeichenfolge die Benutzer-Eingabe gespeichert werden soll. Die volle Aufgabe von `read_line` besteht darin, alles, was der Benutzer in die Standardeingabe eingibt, anzuhängen und das an eine Zeichenfolge anzuhängen (ohne deren Inhalt zu überschreiben), weshalb wir diese Zeichenfolge als Argument übergeben. Das Zeichenfolgenargument muss veränderlich sein, damit die Methode den Inhalt der Zeichenfolge ändern kann.

Das `&` zeigt an, dass dieses Argument eine _Referenz_ ist, die Ihnen eine Möglichkeit gibt, mehreren Teilen Ihres Codes zu ermöglichen, auf ein Stück Daten zuzugreifen, ohne dass Sie das Daten in den Speicher mehrfach kopieren müssen. Referenzen sind ein komplexes Feature, und ein großer Vorteil von Rust ist, wie sicher und einfach es ist, Referenzen zu verwenden. Sie müssen nicht viele Details kennen, um dieses Programm abzuschließen. Im Moment müssen Sie nur wissen, dass, wie Variablen, Referenzen standardmäßig unveränderlich sind. Daher müssen Sie `&mut guess` schreiben, anstatt `&guess`, um sie veränderlich zu machen. (Kapitel 4 wird Referenzen ausführlicher erklären.)
