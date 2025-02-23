# Signale

In einigen Fällen möchten wir, dass unsere Go-Programme Unix-Signale intelligent behandeln. Beispielsweise möchten wir, dass ein Server sich ordnungsgemäß herunterfährt, wenn er ein `SIGTERM` erhält, oder dass ein Befehlszeilentool die Eingabeverarbeitung stoppt, wenn es ein `SIGINT` erhält.

## Anforderungen

- Erstellen eines gepufferten Kanals, um `os.Signal`-Benachrichtigungen zu empfangen.
- Registrieren des Kanals, um Benachrichtigungen über bestimmte Signale mithilfe von `signal.Notify` zu empfangen.
- Erstellen eines Goroutines, um einen blockierenden Empfang von Signalen auszuführen.
- Ausgeben des empfangenen Signals und Benachrichtigen des Programms, dass es beendet werden kann.
- Warten auf das erwartete Signal und dann beenden.

## Beispiel

```sh
# Wenn wir dieses Programm ausführen, wird es blockieren und auf ein
# Signal warten. Indem wir `ctrl-C` eingeben (was der
# Terminal als `^C` anzeigt), können wir ein `SIGINT`-Signal senden,
# was das Programm veranlasst, `interrupt` auszugeben und dann zu beenden.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```
