# Einführung

In diesem Lab wird gezeigt, wie verschiedene Aufbereitungs- und Merkmalsgewinnungspipelines auf verschiedene Teilmengen von Merkmalen angewendet werden können, indem `ColumnTransformer` verwendet wird. Dies ist besonders nützlich bei Datensätzen, die heterogene Datentypen enthalten, da wir möglicherweise die numerischen Merkmale skalieren und die kategorischen Merkmale mit One-Hot-Codierung versehen möchten.

In diesem Lab verwenden wir den Titanic-Datensatz von OpenML, um eine Pipeline zu erstellen, die sowohl kategorische als auch numerische Daten mit `ColumnTransformer` aufbereitet und diese verwendet, um ein logistisches Regressionsmodell zu trainieren.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
