# Einführung

Principal Component Regression (PCR) und Partial Least Squares Regression (PLS) sind zwei Methoden, die in der Regressionsanalyse eingesetzt werden. Beim PCR wird die PCA auf die Trainingsdaten angewendet, gefolgt von der Ausbildung eines Regressors auf den transformierten Proben. Die PCA-Transformation ist unüberwacht, was bedeutet, dass keine Informationen über die Ziele verwendet werden. Folglich kann der PCR in einigen Datensätzen schlecht performen, in denen das Ziel stark mit Richtungen korreliert ist, die eine geringe Varianz aufweisen.

PLS ist sowohl ein Transformator als auch ein Regressor und ähnelt dem PCR ziemlich stark. Es wendet auch eine Dimensionsreduzierung auf die Proben an, bevor ein linearer Regressor auf die transformierten Daten angewendet wird. Der Hauptunterschied zum PCR besteht darin, dass die PLS-Transformation überwacht ist. Daher leidet es nicht unter dem oben genannten Problem.

In diesem Lab werden wir PCR und PLS auf einem Toy-Datensatz vergleichen.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
