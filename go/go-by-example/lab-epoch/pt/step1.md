# Epoch

O problema a ser resolvido neste laboratório é escrever um programa em Golang que possa calcular o número de segundos, milissegundos ou nanossegundos desde a época Unix (Unix epoch).

Para completar este laboratório, você precisa ter um conhecimento básico de Golang e dos seguintes requisitos:

- Familiaridade com o pacote `time` em Golang.
- Conhecimento de como usar as funções `Unix`, `UnixMilli` e `UnixNano` no pacote `time`.

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# Next we'll look at another time-related task: time
# parsing and formatting.
```

A seguir, o código completo:

```go
// A common requirement in programs is getting the number
// of seconds, milliseconds, or nanoseconds since the
// [Unix epoch](https://en.wikipedia.org/wiki/Unix_time).
// Here's how to do it in Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Use `time.Now` with `Unix`, `UnixMilli` or `UnixNano`
	// to get elapsed time since the Unix epoch in seconds,
	// milliseconds or nanoseconds, respectively.
	now := time.Now()
	fmt.Println(now)

	fmt.Println(now.Unix())
	fmt.Println(now.UnixMilli())
	fmt.Println(now.UnixNano())

	// You can also convert integer seconds or nanoseconds
	// since the epoch into the corresponding `time`.
	fmt.Println(time.Unix(now.Unix(), 0))
	fmt.Println(time.Unix(0, now.UnixNano()))
}
```
