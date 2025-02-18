# Speichern von Schlüsseln mit zugehörigen Werten in Hash-Tabellen (Hash Maps)

Die letzte unserer gängigen Sammlungen (Collections) ist die _Hash-Tabelle_ (Hash Map). Der Typ `HashMap<K, V>` speichert eine Zuordnung von Schlüsseln des Typs `K` zu Werten des Typs `V` mithilfe einer _Hash-Funktion_, die bestimmt, wie diese Schlüssel und Werte im Speicher platziert werden. Viele Programmiersprachen unterstützen diese Art von Datenstruktur, verwenden aber oft einen anderen Namen, wie z. B. _Hash_, _Map_, _Objekt_, _Hash-Tabelle_, _Wörterbuch_ oder _assoziatives Array_, um nur einige zu nennen.

Hash-Tabellen sind nützlich, wenn Sie Daten nicht wie bei Vektoren anhand eines Index, sondern anhand eines Schlüssels, der von jedem Typ sein kann, abrufen möchten. Beispielsweise könnten Sie in einem Spiel die Punktzahl jeder Mannschaft in einer Hash-Tabelle verfolgen, in der jeder Schlüssel der Name einer Mannschaft ist und die Werte die Punktzahl jeder Mannschaft darstellen. Bei Angabe eines Mannschaftsnamens können Sie seine Punktzahl abrufen.

In diesem Abschnitt werden wir uns die grundlegende API von Hash-Tabellen ansehen, aber viele weitere nützliche Funktionen verstecken sich in den Funktionen, die von der Standardbibliothek für `HashMap<K, V>` definiert werden. Wie immer, überprüfen Sie die Dokumentation der Standardbibliothek für weitere Informationen.
