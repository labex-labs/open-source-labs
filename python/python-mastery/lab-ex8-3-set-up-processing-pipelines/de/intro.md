# Einführung

In diesem Lab lernen Sie, wie Sie Coroutinen (Korrekturen) verwenden, um Datenverarbeitungspipelines zu erstellen. Coroutinen, eine leistungsstarke Python-Funktion, unterstützen kooperatives Multitasking und ermöglichen es Funktionen, die Ausführung anzuhalten und später fortzusetzen.

Die Ziele dieses Labs sind es, zu verstehen, wie Coroutinen in Python funktionieren, Datenverarbeitungspipelines auf der Grundlage von Coroutinen zu implementieren und Daten durch mehrere Coroutinen-Stufen zu transformieren. Sie werden zwei Dateien erstellen: `cofollow.py`, ein auf Coroutinen basierter Dateifollower, und `coticker.py`, eine Aktien-Ticker-Anwendung, die Coroutinen nutzt. Es wird angenommen, dass das Programm `stocksim.py` aus einer früheren Übung weiterhin im Hintergrund läuft und Aktiendaten in einer Protokolldatei generiert.
