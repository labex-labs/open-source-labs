# Prozesse starten

Die Herausforderung erfordert die Implementierung eines Go-Programms, das externe Prozesse startet und deren Ausgabe sammelt.

## Anforderungen

- Das Programm sollte in der Lage sein, externe Prozesse zu starten.
- Das Programm sollte in der Lage sein, die Ausgabe der externen Prozesse zu sammeln.
- Das Programm sollte Fehler behandeln, die während der Ausführung der externen Prozesse auftreten können.

## Beispiel

```sh
# Die gestarteten Programme geben die gleiche Ausgabe zurück,
# als hätten wir sie direkt von der Befehlszeile ausgeführt.
$ go run spawning-processes.go
> date
Do 05. Mai 2022 22:10:12 PDT

# date hat keine `-x`-Flag, daher wird es mit einer
# Fehlermeldung und einem nicht-nullen Rückgabecode beendet.
Befehl beendet mit rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Okt 3 16:29.
drwxr-xr-x 91 mark 3.0K Okt 3 12:50..
-rw-r--r-- 1 mark 1.3K Okt 3 16:28 spawning-processes.go
```
