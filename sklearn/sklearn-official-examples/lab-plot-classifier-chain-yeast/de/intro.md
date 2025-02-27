# Einführung

In diesem Lab wird ein Beispiel für die Verwendung einer Klassifiziererkette auf einem mehrfachklassifizierten Datensatz demonstriert. Der Klassifiziererkettenalgorithmus ist eine Modifikation der Problemtransformationsmethode für die mehrfachklassifizierung. Diese Methode nutzt die Korrelation zwischen den Klassen, indem eine Kette binärer Klassifizierer aufgebaut wird. Jedes Modell erhält die Vorhersagen der vorherigen Modelle in der Kette als Merkmale. Wir werden den `yeast`-Datensatz verwenden, der 2417 Datensätze enthält, von denen jeder 103 Merkmale und 14 mögliche Labels hat. Jeder Datensatz hat mindestens ein Label. Als Referenzpunkt trainieren wir zunächst einen logistischen Regressionsklassifizierer für jedes der 14 Labels. Um die Leistung dieser Klassifizierer zu evaluieren, machen wir Vorhersagen auf einem separaten Testdatensatz und berechnen den Jaccard-Wert für jede Probe.

## Tipps für die VM

Nachdem der Start der VM abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen von Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie sofort beheben.
