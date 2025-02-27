# Einführung

In diesem Lab verwenden wir den Spectral Co-Clustering-Algorithmus auf dem Twenty Newsgroups-Datensatz, um die Dokumente zu biclustern. Der Datensatz enthält 20 Kategorien von Dokumenten, und wir werden die Kategorie "comp.os.ms-windows.misc" ausschließen, da sie Beiträge ohne Daten enthält. Die mit TF-IDF vektorisierten Beiträge bilden eine Worthäufigkeitsmatrix, die dann mit Dhillons Spectral Co-Clustering-Algorithmus biclustert wird. Die resultierenden Dokument-Wort-Bicluster zeigen die Teilmengen von Wörtern an, die in diesen Teilmengen von Dokumenten häufiger verwendet werden. Wir werden auch die Dokumente mit MiniBatchKMeans clusteren, um einen Vergleich durchzuführen.

## Tipps für die VM

Nachdem der VM-Start abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und Jupyter Notebook für die Übung zu nutzen.

Manchmal müssen Sie einige Sekunden warten, bis Jupyter Notebook vollständig geladen ist. Die Validierung von Vorgängen kann aufgrund von Einschränkungen in Jupyter Notebook nicht automatisiert werden.

Wenn Sie während des Lernens Probleme haben, können Sie Labby gerne fragen. Geben Sie nach der Sitzung Feedback, und wir werden das Problem für Sie prompt beheben.
