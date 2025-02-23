# Schnittstellen

Das Problem besteht darin, eine Schnittstelle in Go zu implementieren. Wir müssen einfach alle Methoden in der Schnittstelle implementieren. Hier implementieren wir `geometry` für `rect`s und `circle`s.

## Anforderungen

- Implementieren Sie eine Schnittstelle in Go.
- Implementieren Sie alle Methoden in der Schnittstelle.
- Verwenden Sie eine generische `measure`-Funktion, um auf jede `geometry` zu arbeiten.
- Verwenden Sie Instanzen von `circle`- und `rect`-Strukturen als Argumente für `measure`.

## Beispiel

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Um mehr über Go's Schnittstellen zu erfahren, schauen Sie sich diesen
# [tollen Blogbeitrag](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go) an.
```
