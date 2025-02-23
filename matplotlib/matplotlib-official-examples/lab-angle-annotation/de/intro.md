# Einführung

In diesem Tutorial lernen Sie, wie Sie mit Matplotlib ein skalierungsinvarianter Winkelbezeichner erstellen. Winkelannotationen werden häufig verwendet, um Winkel zwischen Linien oder innerhalb von Formen mit einem Kreisbogen zu markieren. Während Matplotlib eine `~.patches.Arc` bietet, ist ein inhärentes Problem, wenn man sie direkt für solche Zwecke verwendet, dass ein Kreisbogen im Datenraum kreisförmig ist, aber im Anzeigeraum nicht notwendigerweise kreisförmig. Auch ist der Radius des Kreisbogens oft am besten in einem Koordinatensystem definiert, das unabhängig von den tatsächlichen Datenkoordinaten ist - zumindest wenn Sie in Ihr Diagramm frei zoomen möchten, ohne dass die Annotation unendlich groß wird. Dies erfordert eine Lösung, bei der der Mittelpunkt des Kreisbogens im Datenraum definiert wird, aber sein Radius in einer physikalischen Maßeinheit wie Punkten oder Pixeln oder als Verhältnis der Achsenabmessung.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
