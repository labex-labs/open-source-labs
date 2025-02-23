# Zeitformatierung und -parsing

Das Problem besteht darin, die Zeit in Golang mit den bereitgestellten Layouts zu formatieren und zu parsen.

## Anforderungen

- Verwenden Sie das `time`-Paket, um die Zeit zu formatieren und zu parsen.
- Verwenden Sie das `time.RFC3339`-Layout, um die Zeit zu formatieren und zu parsen.
- Verwenden Sie die Referenzeit `Mon Jan 2 15:04:05 MST 2006`, um das Muster zu zeigen, mit dem eine gegebene Zeit/Zeichenfolge formatiert/parsiert wird.
- Verwenden Sie die `Parse`-Funktion, um die Zeit zu parsen.
- Verwenden Sie die `Format`-Funktion, um die Zeit zu formatieren.
- Verwenden Sie die `fmt.Println`-Funktion, um die formatierten Zeit auszugeben.
- Verwenden Sie die `fmt.Printf`-Funktion, um die formatierten Zeit mit extrahierten Komponenten auszugeben.

## Beispiel

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006":...
```
