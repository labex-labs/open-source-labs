# Einführung

In diesem Lab lernen Sie über verwaltete Generatoren (managed generators) kennen und verstehen, wie Sie diese auf ungewöhnliche Weise ansteuern können. Sie werden auch einen einfachen Task-Scheduler (Aufgabenplaner) erstellen und einen Netzwerkserver mithilfe von Generatoren entwickeln.

Eine Generatorfunktion in Python erfordert externen Code zur Ausführung. Beispielsweise wird ein Iterationsgenerator nur ausgeführt, wenn er in einer `for`-Schleife iteriert wird, und Coroutinen (Korrekturen) müssen über ihre `send()`-Methode aufgerufen werden. In diesem Lab werden wir praktische Beispiele für die Ansteuerung von Generatoren in fortgeschrittenen Anwendungen untersuchen. Die während dieses Labs erstellten Dateien sind `multitask.py` und `server.py`.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Dies ist ein Guided Lab, das schrittweise Anweisungen bietet, um Ihnen beim Lernen und Üben zu helfen. Befolgen Sie die Anweisungen sorgfältig, um jeden Schritt abzuschließen und praktische Erfahrungen zu sammeln. Historische Daten zeigen, dass dies ein Labor der Stufe <span class="text-green-600 dark:text-green-400">Anfänger</span> mit einer Abschlussquote von <span class="text-green-600 dark:text-green-400">84.21%</span> ist.
</div>
