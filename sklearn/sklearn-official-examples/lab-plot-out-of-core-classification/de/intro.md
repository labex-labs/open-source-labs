# Einführung

Dieses Labor bietet ein Beispiel dafür, wie man scikit-learn für die Textklassifikation mit out-of-core-Lernen verwendet. Ziel ist es, aus Daten zu lernen, die nicht in den Hauptspeicher passen. Dazu verwenden wir einen Online-Klassifizierer, der die partial_fit-Methode unterstützt und mit Batches von Beispielen gefüttert wird. Um sicherzustellen, dass der Merkmalsraum über die Zeit gleich bleibt, nutzen wir einen HashingVectorizer, der jedes Beispiel in den gleichen Merkmalsraum projiziert. Dies ist besonders nützlich bei der Textklassifikation, wenn in jedem Batch neue Merkmale (Wörter) auftauchen können.

## Tipps für die VM

Nachdem der Start der VM abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
