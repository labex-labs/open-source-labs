# Einführung

Hyperparameter sind Parameter, die von einem Schätzer nicht direkt gelernt werden. Sie werden als Argumente an den Konstruktor der Schätzerklassen übergeben. Das Anpassen der Hyperparameter eines Schätzers ist ein wichtiger Schritt bei der Konstruktion effektiver maschineller Lernmodelle. Es beinhaltet das Finden der optimalen Kombination von Hyperparametern, die zu der besten Leistung des Modells führen.

Scikit-learn bietet mehrere Werkzeuge, um die besten Hyperparameter zu suchen: `GridSearchCV` und `RandomizedSearchCV`. In diesem Lab werden wir den Prozess des Anpassens von Hyperparametern mit diesen Werkzeugen durchgehen.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback ab, und wir werden das Problem für Sie prompt beheben.
