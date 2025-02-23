# Zeitgeber

Das Lab erfordert die Implementierung eines Zeitgebers, der für eine bestimmte Zeitspanne wartet und dann feuert. Darüber hinaus sollte der Zeitgeber vor dem Auslösen abgebrochen werden können.

- Das `time`-Paket sollte importiert werden.
- Zwei Zeitgeber sollten erstellt werden, ein Zeitgeber, der 2 Sekunden wartet, und ein anderer, der 1 Sekunde wartet.
- Der erste Zeitgeber sollte "Timer 1 fired" ausgeben, wenn er feuert.
- Der zweite Zeitgeber sollte "Timer 2 fired" ausgeben, wenn er feuert.
- Der zweite Zeitgeber sollte vor dem Auslösen abgebrochen werden.
- Das Programm sollte 2 Sekunden warten, um zu zeigen, dass der zweite Zeitgeber nicht ausgelöst hat.

```sh
// Der erste Zeitgeber wird ~2s nach dem Start des
// Programms feuern, aber der zweite sollte vor dem
// Auslösen gestoppt werden.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```

Hier ist der vollständige Code:

```go
// Wir möchten oft Go-Code zu einem bestimmten Zeitpunkt
// in der Zukunft ausführen oder wiederholt in einem
// bestimmten Intervall. Go's integrierte _Timer_ und
// _Taster_ Funktionen erleichtern beide Aufgaben. Wir
// werden zuerst die Zeitgeber betrachten und dann die
// [Taster](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Zeitgeber repräsentieren ein einzelnes Ereignis in
	// der Zukunft. Sie sagen dem Zeitgeber, wie lange Sie
	// warten möchten, und er liefert einen Kanal, der zu
	// diesem Zeitpunkt benachrichtigt wird. Dieser
	// Zeitgeber wird 2 Sekunden warten.
	timer1 := time.NewTimer(2 * time.Second)

	// Der `<-timer1.C` blockiert auf dem Kanal `C` des
	// Zeitgebers, bis er einen Wert sendet, der angibt,
	// dass der Zeitgeber ausgelöst hat.
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// Wenn Sie nur warten möchten, hätten Sie `time.Sleep`
	// verwenden können. Ein Grund, warum ein Zeitgeber
	// nützlich sein kann, ist, dass Sie den Zeitgeber
	// vor dem Auslösen abbrechen können. Hier ist ein
	// Beispiel dafür.
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}

	// Geben Sie dem `timer2` genug Zeit, um auszulösen,
	// wenn es jemals ausgelöst werden würde, um zu zeigen,
	// dass es tatsächlich gestoppt ist.
	time.Sleep(2 * time.Second)
}

```
