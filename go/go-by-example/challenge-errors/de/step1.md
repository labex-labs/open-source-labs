# Fehler

Die Herausforderung liefert zwei Funktionen, die einen Fehler zurückgeben, wenn das Eingabeargument 42 ist. Die erste Funktion gibt einen einfachen Fehlerwert zurück, während die zweite Funktion einen benutzerdefinierten Typ verwendet, um den Fehler darzustellen.

## Anforderungen

- Das `errors`-Paket muss importiert werden.
- Die `f1`-Funktion muss einen Fehler zurückgeben, wenn das Eingabeargument 42 ist.
- Die `f2`-Funktion muss einen Fehler vom Typ `argError` zurückgeben, wenn das Eingabeargument 42 ist.
- Der `argError`-Typ muss zwei Felder haben: `arg` und `prob`.
- Der `argError`-Typ muss die `Error()`-Methode implementieren.
- Die `main`-Funktion muss sowohl `f1` als auch `f2` mit Eingabeargumenten von 7 und 42 aufrufen.
- Die `main`-Funktion muss das Ergebnis jedes Funktionsaufrufs zusammen mit jedem zurückgegebenen Fehler ausgeben.
- Die `main`-Funktion muss demonstrieren, wie man programmgesteuert die Daten in einem benutzerdefinierten Fehler verwendet.

## Beispiel

```sh
$ go run errors.go
f1 funktionierte: 10
f1 fehlgeschlagen: kann nicht mit 42 arbeiten
f2 funktionierte: 10
f2 fehlgeschlagen: 42 - kann nicht damit arbeiten
42
kann nicht damit arbeiten

# Siehe diesen [tollen Beitrag](https://go.dev/blog/error-handling-and-go)
# auf dem Go-Blog für mehr Informationen zur Fehlerbehandlung.
```
