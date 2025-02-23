# Zusammenfassung

In dieser Herausforderung haben wir gelernt, wie man in Go Timeouts mit Hilfe von Kanälen und `select` implementiert. Wir haben einen gepufferten Kanal verwendet, um Goroutine-Lecks zu vermeiden, falls der Kanal niemals gelesen wird, und `time.After`, um auf einen Wert zu warten, der nach Ablauf der Zeitüberschreitung gesendet wird. Wir haben auch `select` verwendet, um mit der ersten empfangenen Nachricht fortzufahren, die bereit ist.
