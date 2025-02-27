# Einführung

In diesem Lab verwenden wir den Ames Housing-Datensatz, um verschiedene Methoden zum Umgang mit kategorischen Merkmalen in Gradient Boosting-Schätzern zu vergleichen. Der Datensatz enthält sowohl numerische als auch kategorische Merkmale, und das Ziel ist der Verkaufspreis der Häuser. Wir werden die Leistung von vier verschiedenen Pipelines vergleichen:

- Das Entfernen der kategorischen Merkmale
- Die One-Hot-Codierung der kategorischen Merkmale
- Das Behandeln der kategorischen Merkmale als ordinalwerte
- Das Verwenden der nativen Kategorieunterstützung in der Gradient Boosting-Schätzung

Wir werden die Pipelines in Bezug auf ihre Anpassungszeiten und Vorhersageleistungen mithilfe von Kreuzvalidierung bewerten.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
