# Einführung

In diesem Lab werden wir lernen, wie man die Varianz der Receiver Operating Characteristic (ROC)-Metrik mit Hilfe von Kreuzvalidierung in Python abschätzt und visualisiert. ROC-Kurven werden bei der binären Klassifikation verwendet, um die Leistung eines Modells zu messen, indem die wahre Positivrate (TPR) gegen die falsche Positivrate (FPR) aufgetragen wird. Wir werden die Scikit-learn-Bibliothek verwenden, um den Iris-Datensatz zu laden, rauschende Merkmale zu erstellen und den Datensatz mit Support Vector Machine (SVM) zu klassifizieren. Anschließend werden wir die ROC-Kurven mit Kreuzvalidierung plotten und die durchschnittliche Fläche unter der Kurve (AUC) berechnen, um die Variabilität der Klassifikatorausgabe zu sehen, wenn der Trainingssatz in verschiedene Teilmengen unterteilt wird.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
