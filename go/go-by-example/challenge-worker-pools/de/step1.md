# Worker-Pools

Implementieren Sie einen Worker-Pool, der Arbeit über den `jobs`-Kanal empfängt und die entsprechenden Ergebnisse über den `results`-Kanal sendet. Der Worker-Pool sollte mehrere parallele Instanzen haben, und jeder Worker sollte pro Aufgabe eine Sekunde schlafen, um eine aufwendige Aufgabe zu simulieren.

## Anforderungen

- Verwenden Sie Goroutines und Kanäle, um den Worker-Pool zu implementieren.
- Der Worker-Pool sollte mehrere parallele Instanzen haben.
- Jeder Worker sollte pro Aufgabe eine Sekunde schlafen, um eine aufwendige Aufgabe zu simulieren.
- Der Worker-Pool sollte Arbeit über den `jobs`-Kanal empfangen und die entsprechenden Ergebnisse über den `results`-Kanal senden.

## Beispiel

```sh
# Unser laufendes Programm zeigt die 5 Aufgaben, die von
# verschiedenen Arbeitern ausgeführt werden. Das Programm benötigt nur etwa 2 Sekunden,
# obwohl insgesamt etwa 5 Sekunden Arbeit zu erledigen sind, weil
# es 3 Arbeiter gibt, die gleichzeitig arbeiten.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```
