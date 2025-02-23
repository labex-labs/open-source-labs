# Channel Puffering

Standardmäßig sind Kanäle in Golang unpuffernd, was bedeutet, dass sie nur Sendevorgänge akzeptieren, wenn es einen entsprechenden Empfang gibt, der bereit ist, den gesendeten Wert zu empfangen. Buffered Kanäle akzeptieren jedoch eine begrenzte Anzahl von Werten ohne einen entsprechenden Empfänger für diese Werte. In dieser Herausforderung müssen Sie einen buffered Channel erstellen und Werte in den Channel senden, ohne dass es einen entsprechenden parallelen Empfang gibt.

## Anforderungen

- Grundkenntnisse von Golang-Kanälen
- Verständnis von buffered Kanälen

## Beispiel

```sh
$ go run channel-buffering.go
buffered
channel
```
