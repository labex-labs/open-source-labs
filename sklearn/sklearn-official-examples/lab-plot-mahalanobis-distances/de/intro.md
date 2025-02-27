# Einführung

In diesem Lab werden wir die Verwendung der robusten Kovarianzschätzung mit Mahalanobis-Distanzen für gaussverteilt Daten untersuchen. Die Mahalanobis-Distanz misst die Entfernung zwischen einem Punkt und einer Verteilung. Sie wird definiert als die Entfernung zwischen einem Punkt und dem Mittelwert der Verteilung, skaliert mit der Inverse der Kovarianzmatrix der Verteilung. Für gaussverteilt Daten kann die Mahalanobis-Distanz verwendet werden, um die Entfernung einer Beobachtung zum Modalwert der Verteilung zu berechnen. Wir werden die Leistung des Minimum Covariance Determinant (MCD)-Schätzers, eines robusten Schätzers für die Kovarianz, mit dem Standard-Kovarianz-Maximum-Likelihood-Schätzer (MLE) bei der Berechnung der Mahalanobis-Distanzen eines kontaminierten Datensatzes vergleichen.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
