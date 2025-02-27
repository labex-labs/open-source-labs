# Einführung

In diesem Lab wird gezeigt, wie die scikit-learn-API verwendet wird, um einen großen Datensatz von Gesichtern zu verarbeiten und einen Satz von 20 x 20-Bildausschnitten zu lernen, die Gesichter repräsentieren. Der Schlüsselaspekt dieses Labs ist die Verwendung des Online-Lernens, bei dem wir Bilder nacheinander laden und verarbeiten und 50 zufällige Ausschnitte aus jedem Bild extrahieren. Wir sammeln 500 Ausschnitte (aus 10 Bildern) und führen dann die partielle_fit-Methode des Online-KMeans-Objekts MiniBatchKMeans aus.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby fragen. Geben Sie nach der Sitzung Feedback ab, und wir werden das Problem für Sie prompt beheben.
