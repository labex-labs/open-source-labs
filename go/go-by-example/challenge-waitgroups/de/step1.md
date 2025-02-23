# waitgroups

Das Problem, das in dieser Herausforderung gelöst werden muss, besteht darin, mehrere Goroutinen zu starten und den Wartezähler der WaitGroup um eins zu erhöhen, für jede einzelne. Anschließend müssen wir auf das Ende aller gestarteten Goroutinen warten.

## Anforderungen

- Grundkenntnisse von Golang.
- Verständnis der Konkurrenz in Golang.
- Vertrautheit mit dem `sync`-Paket.

## Beispiel

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# Die Reihenfolge, in der die Worker starten und beenden,
# wird bei jeder Ausführung wahrscheinlich unterschiedlich sein.
```
