# Einführung

In diesem Lab wird gezeigt, wie man die k nächsten Nachbarn im Voraus berechnet, bevor man sie in KNeighborsClassifier verwendet. KNeighborsClassifier kann die nächsten Nachbarn intern berechnen, aber das Vorher-Berechnen kann mehrere Vorteile haben, wie eine feinere Parametersteuerung, das Cachen für mehrfaches Verwenden oder benutzerdefinierte Implementierungen. Hier verwenden wir die Caching-Eigenschaft von Pipelines, um den Nachbargraphen zwischen mehreren Anpassungen von KNeighborsClassifier zu cachen.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
