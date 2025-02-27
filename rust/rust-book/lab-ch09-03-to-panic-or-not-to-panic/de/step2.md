# Beispiele, Prototyp-Code und Tests

Wenn du ein Beispiel schreibst, um ein bestimmtes Konzept zu veranschaulichen, kann das Einbeziehen von robustem Fehlerbehandlungs-Code das Beispiel unklarer machen. In Beispielen ist es verständlich, dass ein Aufruf einer Methode wie `unwrap`, die in Panik geraten kann, als Platzhalter für die Art und Weise gedacht ist, wie deine Anwendung Fehler behandeln soll, was je nach dem, was der Rest deines Codes macht, variieren kann.

Ähnlich sind die Methoden `unwrap` und `expect` sehr praktisch beim Prototyping, bevor du bereit bist, zu entscheiden, wie du Fehler behandeln willst. Sie hinterlassen klare Markierungen in deinem Code, wann du bereit bist, dein Programm robuster zu gestalten.

Wenn ein Methodenaufruf in einem Test fehlschlägt, willst du, dass der gesamte Test fehlschlägt, auch wenn diese Methode nicht die zu testende Funktionalität ist. Da `panic!` die Art und Weise ist, wie ein Test als fehlgeschlagen markiert wird, sollte genau das passieren, wenn du `unwrap` oder `expect` aufrufst.
