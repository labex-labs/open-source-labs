# Rate Limiting

Das Problem besteht darin, die Verarbeitung eingehender Anfragen zu begrenzen, um die Dienstqualität aufrechtzuerhalten und die Ressourcennutzung zu steuern.

## Anforderungen

- Go-Programmiersprache
- Grundlegendes Verständnis von Goroutinen, Kanälen und Tastern

## Beispiel

```sh
# Wenn wir unser Programm ausführen, sehen wir, dass die erste Batch-Anfragen
# wie gewünscht einmal alle ~200 Millisekunden behandelt werden.
$ go run rate-limiting.go
request 1 2012-10-19 00:38:18.687438 +0000 UTC
request 2 2012-10-19 00:38:18.887471 +0000 UTC
request 3 2012-10-19 00:38:19.087238 +0000 UTC
request 4 2012-10-19 00:38:19.287338 +0000 UTC
request 5 2012-10-19 00:38:19.487331 +0000 UTC

# Für die zweite Batch-Anfragen servieren wir die ersten
# 3 sofort aufgrund des burstbaren Rate Limitings,
# und servieren dann die verbleibenden 2 mit jeweils ~200ms Verzögerung.
request 1 2012-10-19 00:38:20.487578 +0000 UTC
request 2 2012-10-19 00:38:20.487645 +0000 UTC
request 3 2012-10-19 00:38:20.487676 +0000 UTC
request 4 2012-10-19 00:38:20.687483 +0000 UTC
request 5 2012-10-19 00:38:20.887542 +0000 UTC
```
