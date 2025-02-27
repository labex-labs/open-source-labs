# Einführung

In diesem Lab werden wir demonstrieren, wie man mit dem RANSAC-Algorithmus in scikit-learn eine lineare Modell robust an fehlerhafte Daten anpassen kann. Der gewöhnliche lineare Regressor ist empfindlich gegenüber Ausreißern, und die gefittete Linie kann leicht von der wahren zugrunde liegenden Beziehung der Daten abgelenkt werden. Der RANSAC-Regressor teilt die Daten automatisch in Inlier und Outlier auf, und die gefittete Linie wird nur durch die identifizierten Inlier bestimmt. Wir werden das make_regression-Dataset aus scikit-learn verwenden, um zufällige Daten mit Ausreißern zu generieren, und anschließend sowohl ein lineares Modell als auch einen RANSAC-Regressor an die Daten anpassen.

## VM-Tipps

Nachdem die VM gestartet ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
