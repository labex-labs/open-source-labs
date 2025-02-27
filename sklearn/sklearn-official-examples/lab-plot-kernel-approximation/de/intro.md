# Einführung

In diesem Lab wird die Approximation der Feature Map eines RBF-Kernels mithilfe von RBFSampler und Nystroem veranschaulicht, um die Feature Map eines RBF-Kernels für die Klassifizierung mit einem SVM auf dem Digits-Dataset zu approximieren. Es werden die Ergebnisse eines linearen SVM im ursprünglichen Raum, eines linearen SVM mit den approximativen Abbildungen und eines kernelisierten SVM verglichen. Es werden Laufzeiten und Genauigkeiten für unterschiedliche Mengen an Monte Carlo-Stichproben (im Falle von RBFSampler, der zufällige Fourier-Features verwendet) und verschiedene Größen von Teilmengen des Trainingssets (für Nystroem) für die approximative Abbildung gezeigt.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
