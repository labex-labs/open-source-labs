# Einführung

In diesem Tutorial wird gezeigt, wie mit scikit-learn Quantil-Regression durchgeführt werden kann. Wir werden zwei synthetische Datensätze generieren, um zu veranschaulichen, wie die Quantil-Regression nicht-triviale bedingte Quantile prognostizieren kann. Wir werden die Klasse `QuantileRegressor` verwenden, um den Median sowie ein niedriges und ein hohes Quantil zu schätzen, die jeweils auf 5 % und 95 % festgelegt sind. Wir werden `QuantileRegressor` mit `LinearRegression` vergleichen und deren Leistung mithilfe des mittleren absoluten Fehlers (MAE) und des mittleren quadratischen Fehlers (MSE) bewerten.

## Tipps für die VM

Nachdem der Start der VM abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen von Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
