# Einführung

In diesem Lab wird gezeigt, wie die polynomielle Kernapproximation in scikit-learn verwendet werden kann, um effizient Approximationen des polynomiellen Kern-Funktionsraums zu generieren. Dies wird verwendet, um lineare Klassifizierer zu trainieren, die die Genauigkeit von kernbasierten Klassifizierern approximieren. Wir werden den Covtype-Datensatz verwenden, der 581.012 Samples mit jeweils 54 Merkmalen enthält, die auf 6 Klassen verteilt sind. Ziel dieses Datensatzes ist es, die Waldbedeckungstypen ausschließlich aus kartographischen Variablen (ohne Fernerkundungsdaten) vorherzusagen. Nachdem wir ihn geladen haben, transformieren wir ihn in ein binäres Klassifizierungsproblem, um der Version des Datensatzes auf der LIBSVM-Webseite zu entsprechen, die in der ursprünglichen Veröffentlichung verwendet wurde.

## Tipps für die VM

Nachdem der Start der VM abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen von Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
