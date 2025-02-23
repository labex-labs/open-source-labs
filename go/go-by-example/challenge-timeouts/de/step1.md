# Timeouts

Wenn Programme sich an externe Ressourcen anschließen oder die Ausführungszeit begrenzen müssen, sind Timeouts wichtig. Die Herausforderung besteht darin, Timeouts in Go mit Hilfe von Kanälen und `select` zu implementieren.

## Anforderungen

- Implementieren Sie Timeouts in Go mit Hilfe von Kanälen und `select`.
- Verwenden Sie einen gepufferten Kanal, um Goroutine-Lecks zu vermeiden, falls der Kanal niemals gelesen wird.
- Verwenden Sie `time.After`, um auf einen Wert zu warten, der nach Ablauf der Zeitüberschreitung gesendet wird.
- Verwenden Sie `select`, um mit der ersten empfangenen Nachricht fortzufahren, die bereit ist.

## Beispiel

```sh
# Wenn Sie dieses Programm ausführen, wird die erste Operation
# aufgrund der Zeitüberschreitung abgebrochen und die zweite
# erfolgreich ausgeführt.
$ go run timeouts.go
timeout 1
result 2
```
