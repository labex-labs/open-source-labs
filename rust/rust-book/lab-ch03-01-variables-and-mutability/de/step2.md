# Konstanten

Ähnlich wie unveränderliche Variablen sind _Konstanten_ Werte, die an einen Namen gebunden sind und nicht geändert werden dürfen, aber es gibt einige Unterschiede zwischen Konstanten und Variablen.

Zunächst ist es nicht möglich, `mut` mit Konstanten zu verwenden. Konstanten sind nicht nur standardmäßig unveränderlich - sie sind immer unveränderlich. Sie deklarieren Konstanten mit dem Schlüsselwort `const` anstelle des `let`-Schlüsselworts, und der Typ des Werts _muss_ annotiert werden. Wir werden in "Datentypen" auf Typen und Typannotationen eingehen, also brauchen Sie sich jetzt nicht um die Details zu kümmern. Einfach wissen, dass Sie immer den Typ annotieren müssen.

Konstanten können in jedem Gültigkeitsbereich deklariert werden, einschließlich des globalen Gültigkeitsbereichs, was sie für Werte nützlich macht, über die viele Teile des Codes informiert sein müssen.

Der letzte Unterschied ist, dass Konstanten nur einem Konstantenausdruck zugewiesen werden können, nicht dem Ergebnis eines Werts, der nur zur Laufzeit berechnet werden kann.

Hier ist ein Beispiel für eine Konstantendeklaration:

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

Der Name der Konstante ist `THREE_HOURS_IN_SECONDS` und ihr Wert ist auf das Ergebnis der Multiplikation von 60 (der Anzahl der Sekunden in einer Minute) mit 60 (der Anzahl der Minuten in einer Stunde) mit 3 (der Anzahl der Stunden, die wir in diesem Programm zählen möchten) gesetzt. Rusts Namenskonvention für Konstanten ist, alle Großbuchstaben zu verwenden und Unterstriche zwischen den Wörtern. Der Compiler kann eine begrenzte Anzahl von Operationen zur Compile-Zeit auswerten, was uns ermöglicht, diesen Wert auf eine Weise zu schreiben, die einfacher zu verstehen und zu verifizieren ist, anstatt diese Konstante auf den Wert `10.800` zu setzen. Weitere Informationen über die Operationen, die bei der Deklaration von Konstanten verwendet werden können, finden Sie im Abschnitt zur Konstantenauswertung in der Rust-Referenz unter *https://doc.rust-lang.org/reference/const_eval.html*.

Konstanten sind für die gesamte Laufzeit eines Programms gültig, innerhalb des Gültigkeitsbereichs, in dem sie deklariert wurden. Diese Eigenschaft macht Konstanten nützlich für Werte in Ihrem Anwendungsbereich, über die mehrere Teile des Programms informiert sein müssen, wie die maximale Anzahl von Punkten, die ein Spieler eines Spiels erreichen darf, oder die Lichtgeschwindigkeit.

Das Benennen von hartcodierten Werten, die im gesamten Programm verwendet werden, als Konstanten ist hilfreich, um die Bedeutung dieses Werts für zukünftige Wartende des Codes zu vermitteln. Es hilft auch, nur einen einzigen Ort im Code zu haben, an dem Sie ändern müssen, wenn der hartcodierte Wert in Zukunft aktualisiert werden muss.
