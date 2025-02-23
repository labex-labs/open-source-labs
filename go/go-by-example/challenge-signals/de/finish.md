# Zusammenfassung

Die Signals-Ausforderung zeigt, wie man Unix-Signale in Go-Programmen mit Kanälen behandelt. Indem man einen gepufferten Kanal zum Empfang von `os.Signal`-Benachrichtigungen erstellt und den Kanal registriert, um Benachrichtigungen über bestimmte Signale mithilfe von `signal.Notify` zu empfangen, kann man Signale ordnungsgemäß behandeln und das Programm beenden, wenn das erwartete Signal empfangen wird.
