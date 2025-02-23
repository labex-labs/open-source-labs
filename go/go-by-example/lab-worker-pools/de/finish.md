# Zusammenfassung

In diesem Lab wurde gezeigt, wie man einen Worker-Pool mit Goroutines und Kanälen implementiert. Der Worker-Pool empfängt Arbeit über den `jobs`-Kanal und sendet die entsprechenden Ergebnisse über den `results`-Kanal. Jeder Worker schläft pro Aufgabe eine Sekunde, um eine aufwendige Aufgabe zu simulieren.
