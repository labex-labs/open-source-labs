# Einführung

In diesem Lab lernen Sie über verwaltete Generatoren (managed generators) kennen und verstehen, wie Sie diese auf ungewöhnliche Weise ansteuern können. Sie werden auch einen einfachen Task-Scheduler (Aufgabenplaner) erstellen und einen Netzwerkserver mithilfe von Generatoren entwickeln.

Eine Generatorfunktion in Python erfordert externen Code zur Ausführung. Beispielsweise wird ein Iterationsgenerator nur ausgeführt, wenn er in einer `for`-Schleife iteriert wird, und Coroutinen (Korrekturen) müssen über ihre `send()`-Methode aufgerufen werden. In diesem Lab werden wir praktische Beispiele für die Ansteuerung von Generatoren in fortgeschrittenen Anwendungen untersuchen. Die während dieses Labs erstellten Dateien sind `multitask.py` und `server.py`.
