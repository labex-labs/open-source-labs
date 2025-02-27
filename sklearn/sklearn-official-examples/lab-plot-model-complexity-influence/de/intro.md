# Einführung

In diesem Lab werden wir untersuchen, wie die Modellkomplexität sowohl die Vorhersagegenauigkeit als auch die Rechenleistung beeinflusst. Wir werden zwei Datensätze verwenden: den Diabetes-Datensatz für die Regression und den 20newsgroups-Datensatz für die Klassifikation. Wir werden die Komplexitätseffekte auf drei verschiedene Schätzer modellieren:

- SGDClassifier (für Klassifikationsdaten), der das stochastische Gradientenabstieg-Lernen implementiert
- NuSVR (für Regressionsdaten), der die Nu-Support-Vektor-Regression implementiert
- GradientBoostingRegressor, der ein additives Modell in einer vorwärts-stufweisen Weise aufbaut

Wir werden die Modellkomplexität durch die Auswahl relevanter Modellparameter in jedem unserer ausgewählten Modelle variieren. Anschließend werden wir den Einfluss auf die Rechenleistung (Latenz) und die Vorhersagekraft (MSE oder Hamming-Verlust) messen.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie sofort beheben.
