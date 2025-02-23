# Rate Limiting

Das Problem besteht darin, die Verarbeitung eingehender Anfragen zu begrenzen, um die Dienstqualität aufrechtzuerhalten und die Ressourcenauslastung zu steuern.

- Go-Programmiersprache
- Grundlegendes Verständnis von Goroutinen, Kanälen und Tastern

```sh
# Wenn wir unser Programm ausführen, sehen wir, dass die erste
# Batch von Anfragen wie gewünscht einmal alle ~200 Millisekunden
# behandelt wird.
$ go run rate-limiting.go
request 1 2012-10-19 00:38:18.687438 +0000 UTC
request 2 2012-10-19 00:38:18.887471 +0000 UTC
request 3 2012-10-19 00:38:19.087238 +0000 UTC
request 4 2012-10-19 00:38:19.287338 +0000 UTC
request 5 2012-10-19 00:38:19.487331 +0000 UTC

# Für die zweite Batch von Anfragen servieren wir die ersten
# 3 sofort aufgrund des burstfähigen Rate Limitings und
# servieren dann die verbleibenden 2 mit jeweils ~200ms Verzögerung.
request 1 2012-10-19 00:38:20.487578 +0000 UTC
request 2 2012-10-19 00:38:20.487645 +0000 UTC
request 3 2012-10-19 00:38:20.487676 +0000 UTC
request 4 2012-10-19 00:38:20.687483 +0000 UTC
request 5 2012-10-19 00:38:20.887542 +0000 UTC
```

Das vollständige Codebeispiel finden Sie hier unten:

```go
// [_Rate limiting_](https://en.wikipedia.org/wiki/Rate_limiting)
// ist ein wichtiges Mechanismus zur Steuerung der Ressourcenauslastung
// und zur Aufrechterhaltung der Dienstqualität. Go unterstützt
// Rate Limiting elegant mit Goroutinen, Kanälen und [Tastern](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Zunächst betrachten wir das grundlegende Rate Limiting. Angenommen,
	// wir möchten die Verarbeitung eingehender Anfragen begrenzen.
	// Wir servieren diese Anfragen über einen Kanal gleichen Namens.
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	// Dieser `limiter`-Kanal wird alle 200 Millisekunden einen Wert
	// empfangen. Dies ist der Regler in unserem Rate Limiting-Schema.
	limiter := time.Tick(200 * time.Millisecond)

	// Indem wir auf einen Empfang vom `limiter`-Kanal blockieren,
	// bevor wir jede Anfrage servieren, beschränken wir uns auf
	// 1 Anfrage alle 200 Millisekunden.
	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// Wir möchten möglicherweise in unserem Rate Limiting-Schema
	// kurze Ausbrüche von Anfragen zulassen, während wir das
	// Gesamt-Rate Limit beibehalten. Wir können dies erreichen,
	// indem wir unseren limiter-Kanal puffernd gestalten. Dieser
	// `burstyLimiter`-Kanal wird Ausbrüche von bis zu 3 Ereignissen
	// zulassen.
	burstyLimiter := make(chan time.Time, 3)

	// Füllen Sie den Kanal auf, um das erlaubte Ausbrechen darzustellen.
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	// Alle 200 Millisekunden versuchen wir, einen neuen Wert
	// in `burstyLimiter` hinzuzufügen, bis zu seiner Grenze von 3.
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			burstyLimiter <- t
		}
	}()

	// Simulieren Sie nun 5 weitere eingehende Anfragen. Die ersten
	// 3 davon profitieren von der Ausbruchfähigkeit von `burstyLimiter`.
	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)
	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
}

```
