# Verwenden von Threads, um Code gleichzeitig auszuführen

In den meisten aktuellen Betriebssystemen wird der Code eines ausgeführten Programms in einem _Prozess_ ausgeführt, und das Betriebssystem verwaltet mehrere Prozesse gleichzeitig. Innerhalb eines Programms können Sie auch unabhängige Teile haben, die gleichzeitig ausgeführt werden. Die Funktionen, die diese unabhängigen Teile ausführen, werden _Threads_ genannt. Beispielsweise könnte ein Webserver mehrere Threads haben, sodass er gleichzeitig auf mehrere Anfragen reagieren kann.

Das Aufteilen der Berechnung in Ihrem Programm in mehrere Threads, um mehrere Aufgaben gleichzeitig auszuführen, kann die Leistung verbessern, aber es fügt auch Komplexität hinzu. Da Threads gleichzeitig ausgeführt werden können, gibt es keine inhärente Garantie darüber, in welcher Reihenfolge die Teile Ihres Codes auf verschiedenen Threads ausgeführt werden. Dies kann zu Problemen führen, wie:

- Wettlaufbedingungen, bei denen Threads Daten oder Ressourcen in einer inkonsistenten Reihenfolge zugreifen
- Deadlocks, bei denen zwei Threads aufeinander warten und dadurch verhindern, dass beide Threads fortfahren
- Fehler, die nur in bestimmten Situationen auftreten und schwer zu reproduzieren und zu beheben sind

Rust versucht, die negativen Auswirkungen der Verwendung von Threads zu mildern, aber das Programmieren in einem multithreaded Kontext erfordert dennoch sorgfältiges Denken und erfordert eine Code-Struktur, die sich von der in Programmen unterscheidet, die in einem einzelnen Thread ausgeführt werden.

Programmiersprachen implementieren Threads auf verschiedene Weise, und viele Betriebssysteme bieten eine API, die die Sprache aufrufen kann, um neue Threads zu erstellen. Die Rust-Standardbibliothek verwendet ein _1:1_-Modell der Thread-Implementierung, bei dem ein Programm pro einem Sprach-Thread einen Betriebssystem-Thread verwendet. Es gibt Crates, die andere Modelle der Threading implementieren, die andere Kompromisse gegenüber dem 1:1-Modell machen.
