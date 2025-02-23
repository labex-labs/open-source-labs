# Zusammenfassung

Das Signals Lab zeigt, wie man in Go-Programmen mit Kanälen Unix-Signale behandelt. Indem man einen gepufferten Kanal zur Empfang von `os.Signal`-Benachrichtigungen erstellt und den Kanal zur Empfang von Benachrichtigungen über bestimmte Signale mit `signal.Notify` registriert, kann man Signale gnädig behandeln und das Programm beenden, wenn das erwartete Signal empfangen wird.
