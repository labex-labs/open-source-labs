# Einführung

Der stochastische Gradientenabstieg (Stochastic Gradient Descent, SGD) ist ein beliebtes Optimierungsalgorithmus in der Maschinellen Lernens. Es ist eine Variante des Gradientenabstiegsalgorithmus, der bei jeder Iteration eine zufällig ausgewählte Teilmenge der Trainingsdaten verwendet. Dies macht es rechnerisch effizient und geeignet für die Verarbeitung großer Datensätze. In diesem Lab werden wir die Schritte zur Implementierung von SGD in Python mit scikit-learn durchgehen.

## Tipps für die virtuelle Maschine (VM)

Nachdem die VM gestartet wurde, klicken Sie in der oberen linken Ecke auf die Registerkarte **Notebook**, um auf Jupyter Notebook für die Übung zuzugreifen.

Manchmal müssen Sie möglicherweise einige Sekunden warten, bis Jupyter Notebook fertig geladen hat. Die Validierung von Operationen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie sich gerne an Labby wenden. Geben Sie nach der Sitzung Feedback ab, und wir werden das Problem umgehend für Sie lösen.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Dies ist ein Guided Lab, das schrittweise Anweisungen bietet, um Ihnen beim Lernen und Üben zu helfen. Befolgen Sie die Anweisungen sorgfältig, um jeden Schritt abzuschließen und praktische Erfahrungen zu sammeln. Historische Daten zeigen, dass dies ein Labor der Stufe <span class="text-green-600 dark:text-green-400">Anfänger</span> mit einer Abschlussquote von <span class="text-green-600 dark:text-green-400">82%</span> ist. Es hat eine positive Bewertungsrate von <span class="text-primary-600 dark:text-primary-400">100%</span> von den Lernenden erhalten.
</div>
