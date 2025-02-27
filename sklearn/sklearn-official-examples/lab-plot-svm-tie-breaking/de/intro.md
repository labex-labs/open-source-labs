# Einführung

In diesem Lab wird das SVM-Tie-Breaking und seine Auswirkungen auf die Entscheidungsgrenze vorgestellt. Im SVM ist das Tie-Breaking der Mechanismus, der verwendet wird, um Konflikte zwischen zwei oder mehr Klassen zu lösen, wenn ihre Distanzen gleich sind. Es ist standardmäßig nicht aktiviert, wenn `decision_function_shape='ovr'`, da dies aufwendig ist. Daher zeigt dieses Lab die Auswirkungen des Parameters `break_ties` für ein Mehrklassenklassifizierungsproblem und `decision_function_shape='ovr'`.

## VM-Tipps

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu öffnen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund der Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
