# Einführung

Beim maschinellen Lernen bewerten wir die Leistung eines Klassifizierungsmodells oft mithilfe eines Scores. Wir müssen jedoch auch die Signifikanz des Scores testen, um sicherzustellen, dass die Modellleistung nicht rein zufällig ist. Hier kommt der Permutations-Test-Score zum Einsatz. Er generiert eine Nullverteilung, indem er die Genauigkeit des Klassifizierers auf 1000 verschiedenen Permutationen des Datensatzes berechnet. Ein empirischer p-Wert wird dann als das Prozentsatz der Permutationen berechnet, für die der erzielte Score größer ist als der Score, der mit den ursprünglichen Daten erhalten wurde. In diesem Lab verwenden wir die Funktion `permutation_test_score` aus `sklearn.model_selection`, um die Signifikanz eines durch Kreuzvalidierung erhaltenen Scores mithilfe von Permutationen zu evaluieren.

## Tipps für die VM

Nachdem der Start der VM abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen von Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback ab, und wir werden das Problem für Sie prompt beheben.
