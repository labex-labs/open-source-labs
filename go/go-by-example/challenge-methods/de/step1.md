# Methoden

Der bereitgestellte Code definiert einen Strukturtyp namens `rect` mit zwei Feldern, `width` und `height`. Zwei Methoden werden für diesen Strukturtyp definiert, `area` und `perim`. Die `area`-Methode berechnet die Fläche des Rechtecks, und die `perim`-Methode berechnet den Umfang des Rechtecks. Die Hauptfunktion ruft diese beiden Methoden auf und druckt ihre Ergebnisse.

## Anforderungen

- Die `area`-Methode sollte einen Empfänger vom Typ `*rect` haben.
- Die `perim`-Methode sollte einen Empfänger vom Typ `rect` haben.
- Die `area`-Methode sollte die Fläche des Rechtecks zurückgeben.
- Die `perim`-Methode sollte den Umfang des Rechtecks zurückgeben.
- Die `main`-Funktion sollte beide Methoden aufrufen und ihre Ergebnisse drucken.

## Beispiel

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# Als nächstes betrachten wir Go's Mechanismus zum Gruppieren und
# Benennen von verwandten Methodensätzen: Schnittstellen.
```
