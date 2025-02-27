# Einführung

In diesem Lab werden wir lernen, wie wir eine Funktion mit Polynomen bis zu einem bestimmten Grad mit Hilfe von Ridge-Regression approximieren. Wir werden zwei verschiedene Wege zeigen, dies bei `n_samples` eindimensionalen Punkten `x_i` zu tun:

1. `PolynomialFeatures`: Generiert alle Monome bis zu einem angegebenen Grad. Dies gibt uns die Vandermonde-Matrix mit `n_samples` Zeilen und `degree + 1` Spalten.
2. `SplineTransformer`: Generiert B-Spline-Basisfunktionen. Eine Basisfunktion einer B-Spline ist eine stückweise Polynomfunktion vom Grad `degree`, die nur zwischen `degree+1` aufeinanderfolgenden Knoten ungleich Null ist.

Wir werden die `make_pipeline`-Funktion verwenden, um nicht-lineare Merkmale hinzuzufügen, und zeigen, wie diese Transformatoren gut geeignet sind, um nicht-lineare Effekte mit einem linearen Modell zu modellieren. Wir werden die Funktion, die Trainingspunkte und die Interpolation mit Polynommerkmalen und B-Splines plotten. Wir werden auch alle Spalten beider Transformatoren separat plotten und die Knoten der Spline anzeigen. Schließlich werden wir die Verwendung periodischer Splines demonstrieren.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
