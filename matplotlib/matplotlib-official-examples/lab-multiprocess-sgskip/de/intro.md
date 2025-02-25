# Einführung

In diesem Lab lernst du, wie du die `multiprocessing`-Bibliothek und Matplotlib verwendest, um Daten zu visualisieren, die von einem separaten Prozess generiert werden. Wir werden zwei Klassen erstellen - `ProcessPlotter` und `NBPlot` - um die Visualisierung und die Datengenerierung zu verarbeiten. Die `NBPlot`-Klasse wird zufällige Daten generieren und diese über eine Pipe an die `ProcessPlotter`-Klasse senden, die dann die Daten in Echtzeit visualisieren wird.

## Tipps für die VM

Nachdem der Start der VM abgeschlossen ist, klicke in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal musst du einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen von Jupyter Notebook nicht automatisiert werden.

Wenn du während des Lernens Probleme stellst, kannst du Labby gerne fragen. Gib nach der Sitzung Feedback, und wir werden das Problem für dich prompt beheben.
