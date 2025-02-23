# Recover

Die `mayPanic`-Funktion im bereitgestellten Code wird beim Aufruf einen `panic` auslösen. Ihre Aufgabe ist es, die `main`-Funktion zu modifizieren, um von dem `panic` zu recoveren und die Fehlermeldung auszugeben.

## Anforderungen

- Verwenden Sie die `recover`-Funktion, um den `panic` in der `mayPanic`-Funktion zu behandeln.
- Geben Sie die Fehlermeldung aus, wenn ein `panic` auftritt.

## Beispiel

```sh
$ go run recover.go
Recovered. Error:
a problem
```
