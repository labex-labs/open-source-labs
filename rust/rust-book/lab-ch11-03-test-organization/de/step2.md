# Einheitstests

Der Zweck von Einheitstests ist es, jede Codeeinheit isoliert von dem restlichen Code zu testen, um schnell zu ermitteln, wo der Code wie erwartet funktioniert und wo nicht. Du wirst Einheitstests im `src`-Verzeichnis in jeder Datei ablegen, in der sich der zu testende Code befindet. Die Konvention besteht darin, in jeder Datei ein Modul namens `tests` zu erstellen, um die Testfunktionen zu enthalten, und das Modul mit `cfg(test)` zu annotieren.
