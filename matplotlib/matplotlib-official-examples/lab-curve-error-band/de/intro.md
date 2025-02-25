# Einführung

In diesem Tutorial lernen Sie, wie Sie mit Python Matplotlib eine Kurve mit einer Fehlerbande zeichnen. Eine Fehlerbande wird verwendet, um die Unsicherheit der Kurve anzuzeigen. In diesem Beispiel nehmen wir an, dass der Fehler als Skalar _err_ angegeben werden kann, der die Unsicherheit senkrecht zur Kurve in jedem Punkt beschreibt. Wir visualisieren diesen Fehler als eine gefärbte Bande um den Pfad mit einem `.PathPatch`. Der Patch wird aus zwei Pfadsegmenten _(xp, yp)_ und _(xn, yn)_ erstellt, die um +/- _err_ senkrecht zur Kurve _(x, y)_ verschoben werden.

## VM-Tipps

Nachdem die VM gestartet ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
