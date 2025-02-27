# Einführung

In diesem Lab wird gezeigt, wie man Quantil-Regression verwendet, um Prognoseintervalle mit scikit-learn zu erstellen. Wir werden synthetische Daten für ein Regressionsproblem generieren, die Funktion darauf anwenden und Beobachtungen des Ziels mit einer lognormalen Verteilung erstellen. Anschließend teilen wir die Daten in Trainings- und Testdatenmengen auf, trainieren nicht-lineare Quantil- und kleinste Quadrate-Regressoren und erstellen einen gleichmäßig verteilten Evaluierungssatz von Eingabewerten, der den Bereich [0, 10] abdeckt. Wir werden die vorhergesagte Median mit der vorhergesagten Mittelwert vergleichen, die Fehler-Metriken analysieren und den Konfidenzintervall kalibrieren. Schließlich werden wir die Hyperparameter der Quantil-Regressoren optimieren.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback ab, und wir werden das Problem für Sie prompt beheben.
