# Kanalrichtungen

Das Problem, das in diesem Labor gelöst werden soll, besteht darin, den gegebenen Code zu modifizieren, um sicherzustellen, dass die als Funktionsparameter verwendeten Kanäle nur zum Senden oder Empfangen von Werten angegeben werden.

- Grundkenntnisse von Golang
- Verständnis von Kanälen und ihrer Verwendung in Golang

```sh
$ go run channel-directions.go
passed message
```

Hier ist der vollständige Code:

```go
// Wenn Kanäle als Funktionsparameter verwendet werden, können Sie
// angeben, ob ein Kanal nur zum Senden oder Empfangen von
// Werten gedacht ist. Diese Spezifität erhöht die Typsicherheit
// des Programms.

package main

import "fmt"

// Die `ping`-Funktion akzeptiert nur einen Kanal zum Senden
// von Werten. Ein Versuch, von diesem Kanal zu empfangen,
// würde ein Kompilierungsfehler sein.
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// Die `pong`-Funktion akzeptiert einen Kanal zum Empfangen
// (`pings`) und einen zweiten zum Senden (`pongs`).
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}

```
