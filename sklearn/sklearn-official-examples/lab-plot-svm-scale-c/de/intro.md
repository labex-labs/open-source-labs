# Einführung

In diesem Lab wird der Effekt der Skalierung des Regularisierungsparameters bei der Verwendung von Support Vector Machines (SVMs) zur Klassifizierung demonstriert. Bei der SVM-Klassifizierung interessieren wir uns für die Minimierung des Risikos für die Gleichung:

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

wobei:

- `C` wird verwendet, um die Höhe der Regularisierung festzulegen
- `L` ist eine Verlustfunktion unserer Proben und unserer Modellparameter.
- `Ω` ist eine Strafmaßfunktion unserer Modellparameter

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
