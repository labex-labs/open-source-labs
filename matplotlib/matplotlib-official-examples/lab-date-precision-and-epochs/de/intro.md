# Einführung

Dies ist ein schrittweise Tutorial, das zeigt, wie man Datumsgenauigkeit und Epochen in Matplotlib behandelt. Matplotlib kann mit `.datetime`-Objekten und `numpy.datetime64`-Objekten arbeiten, indem es einen Einheitenkonverter verwendet, der diese Daten erkennt und in Gleitkommazahlen umwandelt. Vor Matplotlib 3.3 war die Standardeinstellung für diese Umwandlung ein Float, der die Anzahl der Tage seit "0000-12-31T00:00:00" angab. Ab Matplotlib 3.3 ist die Standardeinstellung die Anzahl der Tage seit "1970-01-01T00:00:00". Dies ermöglicht eine höhere Auflösung für moderne Daten.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
