# Trainiere Klassifizierer

- Erstelle ein logarithmisches Gitter der `gamma`- und `C`-Parameter mit `np.logspace`.
- Teile die Daten in Trainings- und Testsets auf mit `StratifiedShuffleSplit`.
- Führe eine Gittersuche mit `GridSearchCV` durch, um die besten Parameter für das SVM-Modell zu finden.
- Trainiere einen Klassifizierer für alle Parameter in der 2D-Version.
