# Modulausführung

Wenn ein Modul importiert wird, _werden alle Anweisungen im Modul nacheinander ausgeführt_, bis das Ende der Datei erreicht ist. Die Inhalte des Modulnamensraums sind alle _globalen_ Namen, die am Ende des Ausführungsprozesses noch definiert sind. Wenn es Skriptanweisungen gibt, die Aufgaben im globalen Bereich ausführen (Drucken, Erstellen von Dateien usw.), werden Sie sie beim Import ausgeführt sehen.
