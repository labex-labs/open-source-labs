# Einführung

**Ziele:**

- Verwenden von Coroutinen, um Verarbeitungsleitungen aufzubauen

**Erstellte Dateien:** `cofollow.py`, `coticker.py`

**Hinweis**

Für diese Übung sollte das Programm `stocksim.py` weiterhin im Hintergrund laufen.

Im Übungsblatt 8.2 haben Sie Code geschrieben, der Generatoren verwendet hat, um eine Verarbeitungsleitung aufzubauen. Ein wichtiger Aspekt dieses Programms war die Idee, dass Daten zwischen Generatorfunktionen fließen. Ein sehr ähnlicher Datenfluss kann mit Coroutinen aufgebaut werden. Der einzige Unterschied besteht darin, dass Sie mit einer Coroutine Daten in verschiedene Verarbeitungselemente senden, im Gegensatz dazu, dass Sie Daten mit einer for-Schleife herausziehen.
