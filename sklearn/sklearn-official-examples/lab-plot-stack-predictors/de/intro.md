# Einführung

In diesem Lab verwenden wir die Stacking-Methode, um mehrere Schätzer zu kombinieren und Vorhersagen zu treffen. Bei dieser Strategie werden einige Schätzer einzeln auf einem Teilstichproben der Trainingsdaten trainiert, während ein Endschätzer mit den aggregierten Vorhersagen dieser Basis-Schätzer trainiert wird. Wir verwenden den Ames Housing-Datensatz, um den Endpreis der Häuser in Logarithmen zu prognostizieren. Wir verwenden 3 Lerner, linear und nicht-linear, und verwenden einen Ridge-Regressor, um ihre Ausgaben zu kombinieren. Wir vergleichen auch die Leistung jedes einzelnen Prädiktors sowie der Stack der Regressoren.

## Tipps für die VM

Nachdem der Start der VM abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen von Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
