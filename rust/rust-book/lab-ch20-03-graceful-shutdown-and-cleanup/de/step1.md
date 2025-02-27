# Graceful Shutdown and Cleanup

Der Code in Listing 20-20 reagiert wie geplant asynchron auf Anfragen, indem er einen Threadpool verwendet. Wir erhalten einige Warnungen über die Felder `workers`, `id` und `thread`, die wir nicht direkt verwenden, was uns daran erinnert, dass wir nichts bereinigen. Wenn wir die weniger elegante Methode mit Strg+C verwenden, um den Hauptthread zu stoppen, werden auch alle anderen Threads sofort gestoppt, auch wenn sie mitten in der Bearbeitung einer Anfrage sind.

Als nächstes implementieren wir das `Drop`-Trait, um `join` auf jeden Thread im Pool aufzurufen, damit sie die Anfragen, die sie bearbeiten, abschließen können, bevor sie sich schließen. Dann implementieren wir eine Möglichkeit, den Threads mitzuteilen, dass sie keine neuen Anfragen mehr akzeptieren und sich herunterfahren sollten. Um diesen Code in Aktion zu sehen, modifizieren wir unseren Server, sodass er nur zwei Anfragen akzeptiert, bevor er seinen Threadpool gracefully herunterfährt.
