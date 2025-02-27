# Einführung

In diesem Tutorial wird Ihnen der Prozess des Einsatzes von Kernel-Approximationstechniken in scikit-learn erklärt.

Kernel-Methoden wie Support Vector Machines (SVM) sind leistungsstarke Techniken zur nicht-linearen Klassifikation. Diese Methoden basieren auf dem Konzept einer Kernel-Funktion, die die Eingabedaten in einen hochdimensionalen Merkmalsraum abbildet. Arbeiten mit expliziten Merkmalsabbildungen kann jedoch rechenintensiv sein, insbesondere für große Datensätze. Kernel-Approximationsmethoden bieten eine Lösung, indem sie niedrigdimensionale Approximationen des Kernel-Merkmalsraums generieren.

In diesem Tutorial werden wir mehrere Kernel-Approximationstechniken in scikit-learn erkunden, darunter die Nystroem-Methode, die Approximation des Radial Basis Function (RBF)-Kernels, die Approximation des Additive Chi Squared (ACS)-Kernels, die Approximation des Skewed Chi Squared (SCS)-Kernels und die Polynomkernel-Approximation mit Tensor Sketch. Wir werden zeigen, wie diese Techniken verwendet werden, und diskutieren ihre Vor- und Nachteile.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
