# Einführung

In diesem Lab wird gezeigt, wie die Klasse `BayesianGaussianMixture` aus scikit-learn verwendet wird, um einem Toy-Datensatz anzupassen, der eine Mischung von drei Gaußverteilungen enthält. Die Klasse kann automatisch die Anzahl der Mischungskomponenten anpassen, indem sie einen Konzentrations-Prior verwendet, der über das Parameter `weight_concentration_prior_type` angegeben wird. In diesem Lab wird der Unterschied zwischen der Verwendung eines Dirichlet-Verteilungs-Priors und eines Dirichlet-Prozess-Priors gezeigt, um die Anzahl der Komponenten mit nicht-null Gewichten zu wählen.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
