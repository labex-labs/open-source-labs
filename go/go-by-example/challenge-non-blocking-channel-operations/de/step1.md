# Nicht blockierende Kanaloperationen

Das Problem, das in dieser Aufgabe gelöst werden soll, ist die Implementierung nicht blockierender Kanaloperationen mit der `select`-Anweisung mit einer `default`-Klausel.

## Anforderungen

- Implementieren Sie einen nicht blockierenden Empfang über einen Kanal mit der `select`-Anweisung mit einer `default`-Klausel.
- Implementieren Sie einen nicht blockierenden Sendevorgang über einen Kanal mit der `select`-Anweisung mit einer `default`-Klausel.
- Implementieren Sie einen mehrwege-nicht blockierenden Selekt mit der `select`-Anweisung mit mehreren `case`-Klauseln und einer `default`-Klausel.

## Beispiel

```sh
$ go run non-blocking-channel-operations.go
keine Nachricht empfangen
keine Nachricht gesendet
keine Aktivität
```
