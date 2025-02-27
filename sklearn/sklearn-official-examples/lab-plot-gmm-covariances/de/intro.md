# Einführung

In diesem Tutorial wird die Verwendung verschiedener Kovarianztypen für Gaußsche Mischmodelle (GMMs) demonstriert. GMMs werden häufig zur Clusteranalyse verwendet, und wir können die erhaltenen Cluster mit den tatsächlichen Klassen aus dem Datensatz vergleichen. Wir initialisieren die Mittelwerte der Gaußverteilungen mit den Mittelwerten der Klassen aus dem Trainingsset, um diesen Vergleich gültig zu machen. Wir zeichnen vorhergesagte Labels sowohl auf Trainings- als auch auf Testdaten mit einer Vielzahl von GMM-Kovarianztypen auf dem Iris-Datensatz. Wir vergleichen GMMs mit sphärischen, diagonalen, vollen und geketteten Kovarianzmatrizen in aufsteigender Reihenfolge der Leistung.

Obwohl man im Allgemeinen erwarten würde, dass die volle Kovarianz am besten performt, neigt sie dazu, auf kleinen Datensätzen zu overfitten und generalisiert sich nicht gut auf Testdaten.

Auf den Diagrammen werden Trainingsdaten als Punkte und Testdaten als Kreuze dargestellt. Der Iris-Datensatz ist vierdimensional. Hier werden nur die ersten beiden Dimensionen gezeigt, und daher sind einige Punkte in anderen Dimensionen getrennt.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie sofort beheben.
