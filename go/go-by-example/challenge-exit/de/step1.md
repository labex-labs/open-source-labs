# Beenden

Das Problem, das in dieser Aufgabe gelöst werden soll, besteht darin, ein Go-Programm mit einem bestimmten Statuscode zu beenden, indem die `os.Exit`-Funktion verwendet wird.

## Anforderungen

Um diese Aufgabe zu lösen, sollten Sie eine grundlegende Kenntnis von Go-Programmierung und dem `os`-Paket haben.

## Beispiel

```sh
# Wenn Sie `exit.go` mit `go run` ausführen, wird der
# Statuscode von `go` erkannt und ausgegeben.
$ go run exit.go
exit status 3

# Indem Sie eine Binärdatei erstellen und ausführen, können
# Sie den Statuscode im Terminal sehen.
$ go build exit.go
$./exit
$ echo $?
3

# Beachten Sie, dass das `!` aus unserem Programm
# nie ausgegeben wurde.
```
