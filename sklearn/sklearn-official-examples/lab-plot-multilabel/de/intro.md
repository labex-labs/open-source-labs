# Einführung

In diesem Lab wird ein mehrfaches Dokumentklassifizierungsproblem mit scikit-learn demonstriert. Der Datensatz wird zufällig basierend auf dem folgenden Prozess generiert:

- Wähle die Anzahl der Labels: n ~ Poisson(n_labels)
- N-mal wähle eine Klasse c: c ~ Multinomial(theta)
- Wähle die Dokumentlänge: k ~ Poisson(length)
- K-mal wähle ein Wort: w ~ Multinomial(theta_c)

Bei diesem Prozess wird das Verwerfungs-Sampling verwendet, um sicherzustellen, dass n größer als 2 ist und dass die Dokumentlänge niemals Null ist. Ebenso werden bereits gewählte Klassen verworfen. Die Dokumente, die beiden Klassen zugewiesen sind, werden als Punkte umgeben von zwei gefärbten Kreisen geplottet.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicke in der linken oberen Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
