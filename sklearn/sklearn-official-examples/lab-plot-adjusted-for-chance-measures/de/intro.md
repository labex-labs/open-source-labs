# Einführung

In diesem Lab wird der Einfluss einer gleichmäßig verteilten zufälligen Belegung auf das Verhalten einiger Clusterbewertungsmetriken untersucht. Clusteralgorithmen sind im Wesentlichen unüberwachte Lernmethoden, und Bewertungsmetriken, die "überwachte" Ground-Truth-Informationen nutzen, um die Qualität der resultierenden Cluster zu quantifizieren. Nicht angepasste Clusterbewertungsmetriken können jedoch irreführend sein, da sie große Werte für feingranulare Belegungen ausgeben, die völlig zufällig sein können. Daher können nur angepasste Maße sicher als Konsensindex verwendet werden, um die durchschnittliche Stabilität von Clusteralgorithmen für einen gegebenen Wert von k auf verschiedenen überlappenden Teilproben des Datensatzes zu evaluieren.

## VM-Tipps

Nachdem die VM gestartet ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie bei der Lernphase Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Dies ist ein Guided Lab, das schrittweise Anweisungen bietet, um Ihnen beim Lernen und Üben zu helfen. Befolgen Sie die Anweisungen sorgfältig, um jeden Schritt abzuschließen und praktische Erfahrungen zu sammeln. Historische Daten zeigen, dass dies ein Labor der Stufe <span class="text-red-600 dark:text-red-400">Experte</span> mit einer Abschlussquote von <span class="text-red-600 dark:text-red-400">31%</span> ist. Es hat eine positive Bewertungsrate von <span class="text-primary-600 dark:text-primary-400">100%</span> von den Lernenden erhalten.
</div>
