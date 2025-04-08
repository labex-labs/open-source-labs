# Goroutinen

Das Problem, das in dieser Aufgabe gelöst werden soll, ist es, Goroutinen zu erstellen und auszuführen, um Funktionen gleichzeitig auszuführen.

## Anforderungen

- Die `f`-Funktion sollte ihre Eingabezeichenfolge und eine Zählervariable dreimal ausgeben.
- Die `main`-Funktion sollte die `f`-Funktion synchron aufrufen und "direct" und eine Zählervariable dreimal ausgeben.
- Die `main`-Funktion sollte die `f`-Funktion asynchron mithilfe einer Goroutine aufrufen und "goroutine" und eine Zählervariable dreimal ausgeben.
- Die `main`-Funktion sollte eine Goroutine starten, um eine anonyme Funktion auszuführen, die eine Nachricht ausgibt.
- Die `main`-Funktion sollte warten, bis die Goroutinen ihre Ausführung beendet haben, bevor sie "done" ausgibt.

## Beispiel

```sh
# Wenn wir dieses Programm ausführen, sehen wir zuerst die Ausgabe des
# blockierenden Aufrufs, dann die Ausgabe der beiden
# Goroutinen. Die Ausgabe der Goroutinen kann verzahnt sein,
# da die Goroutinen von der Go-Laufzeit gleichzeitig ausgeführt werden.

# Als Nächstes betrachten wir ein Gegenstück zu Goroutinen in
# parallelen Go-Programmen: Kanäle.
```
