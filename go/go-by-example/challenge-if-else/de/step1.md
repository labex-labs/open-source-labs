# if-else

Du musst die Funktion `checkNumber` vervollständigen, die eine Ganzzahl als Eingabe nimmt und einen String zurückgibt. Wenn die Zahl gerade ist, soll "even" zurückgegeben werden, andernfalls soll "odd" zurückgegeben werden.

## Anforderungen

- Die Funktion sollte `checkNumber` heißen.
- Die Funktion sollte eine Ganzzahl als Eingabe nehmen.
- Die Funktion sollte einen String zurückgeben.
- Wenn die Zahl gerade ist, soll "even" zurückgegeben werden.
- Wenn die Zahl ungerade ist, soll "odd" zurückgegeben werden.

## Beispiel

```sh
$ go run if-else.go
7 ist ungerade
8 ist durch 4 teilbar
9 hat 1 Ziffer

# Es gibt kein [ternäres if](https://en.wikipedia.org/wiki/%3F:)
# in Go, daher musst du auch für einfache Bedingungen eine vollständige `if`-Anweisung verwenden.
```
