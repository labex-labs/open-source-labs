# Einführung

Der stochastische Gradientenabstieg ist eine beliebte Optimierungsmethode, die zur Minimierung einer Verlustfunktion verwendet wird. Die Methode führt den Gradientenabstieg schrittweise auf stochastische Weise durch, d. h., indem für jede Iteration zufällig Proben ausgewählt werden. Die Methode ist effizient, insbesondere für die Anpassung linearer Modelle. Allerdings wird die Konvergenz bei jeder Iteration nicht gewährleistet, und die Verlustfunktion muss nicht notwendigerweise bei jeder Iteration abnehmen. In diesem Fall kann es schwierig sein, die Konvergenz der Verlustfunktion zu überwachen. In diesem Lab werden wir die Early-Stopping-Strategie untersuchen, die ein Ansatz zur Überwachung der Konvergenz auf einer Validierungsscore ist. Wir werden das `SGDClassifier`-Modell aus der scikit-learn-Bibliothek und den MNIST-Datensatz verwenden, um zu veranschaulichen, wie Early Stopping verwendet werden kann, um fast die gleiche Genauigkeit wie ein ohne Early Stopping gebautes Modell zu erzielen und die Trainingszeit erheblich zu reduzieren.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
