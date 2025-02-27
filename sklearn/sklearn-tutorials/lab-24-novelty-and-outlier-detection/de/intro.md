# Einführung

Neuerungs- und Ausreißererkennung sind Techniken, die dazu verwendet werden, zu bestimmen, ob eine neue Beobachtung zur gleichen Verteilung wie die vorhandenen Beobachtungen gehört oder ob sie als unterschiedlich betrachtet werden sollte. Diese Techniken werden allgemein verwendet, um reale Datensätze zu bereinigen, indem abnorme oder ungewöhnliche Beobachtungen identifiziert werden.

Es gibt zwei wichtige Unterscheidungen in diesem Zusammenhang:

1. Ausreißererkennung: Die Trainingsdaten enthalten Ausreißer, die Beobachtungen sind, die weit von den anderen entfernt sind. Ausreißererkennungsschätzer versuchen, die Regionen anzupassen, in denen die Trainingsdaten am konzentriertesten sind, und ignorieren die abweichenden Beobachtungen.
2. Neuerungsdetektion: Die Trainingsdaten sind nicht von Ausreißern kontaminiert, und das Ziel ist, zu erkennen, ob eine neue Beobachtung ein Ausreißer ist. In diesem Zusammenhang wird ein Ausreißer auch als Neuerung bezeichnet.

Das scikit-learn-Projekt bietet eine Reihe von Machine-Learning-Tools, die sowohl für die Neuerungs- als auch für die Ausreißererkennung verwendet werden können. Diese Tools werden mit unüberwachten Lernalgorithmen implementiert, was bedeutet, dass sie Muster aus den Daten lernen, ohne dass gelabelte Beispiele erforderlich sind.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
