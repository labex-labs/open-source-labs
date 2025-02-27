# Einführung

Beim Klassifizierungstask ist es oft wichtig, nicht nur das Klassenlabel zu prognostizieren, sondern auch die zugehörige Wahrscheinlichkeit. Die Wahrscheinlichkeit gibt das Vertrauen in die Prognose an. Allerdings liefern nicht alle Klassifizierer gut kalibrierte Wahrscheinlichkeiten, einige sind überzeugt, während andere zu unzuverlässig sind. Eine separate Kalibrierung der vorhergesagten Wahrscheinlichkeiten ist oft als Nachverarbeitung wünschenswert. In diesem Lab werden zwei verschiedene Methoden für diese Kalibrierung gezeigt und die Qualität der zurückgegebenen Wahrscheinlichkeiten mit Hilfe des Brier-Scores bewertet.

## VM-Tipps

Nachdem die VM gestartet ist, klicken Sie in der linken oberen Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen von Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
