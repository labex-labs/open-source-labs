# Einführung

In diesem Lab wird der Einfluss einer gleichmäßig verteilten zufälligen Belegung auf das Verhalten einiger Clusterbewertungsmetriken untersucht. Clusteralgorithmen sind im Wesentlichen unüberwachte Lernmethoden, und Bewertungsmetriken, die "überwachte" Ground-Truth-Informationen nutzen, um die Qualität der resultierenden Cluster zu quantifizieren. Nicht angepasste Clusterbewertungsmetriken können jedoch irreführend sein, da sie große Werte für feingranulare Belegungen ausgeben, die völlig zufällig sein können. Daher können nur angepasste Maße sicher als Konsensindex verwendet werden, um die durchschnittliche Stabilität von Clusteralgorithmen für einen gegebenen Wert von k auf verschiedenen überlappenden Teilproben des Datensatzes zu evaluieren.

## VM-Tipps

Nachdem die VM gestartet ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
