# Einführung

**Ziele:**

- Lernen Sie über verwaltete Generatoren

**Erstellte Dateien:** `multitask.py`, `server.py`

Eine Generator- oder Coroutine-Funktion kann niemals ohne die Unterstützung anderer Code ausgeführt werden. Beispielsweise führt ein Generator, der für die Iteration verwendet wird, nichts aus, es sei denn, die Iteration wird tatsächlich mithilfe einer for-Schleife durchgeführt. Ähnlich wird eine Sammlung von Coroutinen nicht ausgeführt, es sei denn, ihre `send()`-Methode wird auf irgend eine Weise aufgerufen.

In fortgeschrittenen Anwendungen von Generatoren ist es möglich, Generatoren auf verschiedene ungewöhnliche Weise zu steuern. In dieser Übung betrachten wir einige Beispiele.
