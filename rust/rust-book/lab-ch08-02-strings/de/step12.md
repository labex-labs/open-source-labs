# Strings sind nicht so einfach

Zusammenfassend lässt sich sagen, dass Strings kompliziert sind. Verschiedene Programmiersprachen treffen unterschiedliche Entscheidungen darüber, wie diese Komplexität an den Programmierer weitergegeben wird. Rust hat entschieden, das korrekte Handling von `String`-Daten als Standardverhalten für alle Rust-Programme zu machen, was bedeutet, dass Programmierer im Voraus mehr Überlegung in die Behandlung von UTF-8-Daten stecken müssen. Dieser Kompromiss bringt die Komplexität von Strings stärker in den Vordergrund als in anderen Programmiersprachen, verhindert jedoch, dass Sie Fehler bei der Behandlung von nicht-ASCII-Zeichen im späteren Entwicklungsprozess haben müssen.

Die gute Nachricht ist, dass die Standardbibliothek eine Vielzahl von Funktionen bietet, die auf den `String`- und `&str`-Typen aufbauen, um diese komplexen Situationen richtig zu behandeln. Stellen Sie sicher, dass Sie sich die Dokumentation zu hilfreichen Methoden wie `contains` für das Suchen in einem String und `replace` für das Ersetzen von Teilen eines Strings durch einen anderen String ansehen.

Lassen Sie uns zu etwas weniger Komplexem wechseln: Hash-Maps!
