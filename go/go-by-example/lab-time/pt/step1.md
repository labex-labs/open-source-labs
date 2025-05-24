# Tempo

O código abaixo contém exemplos de como trabalhar com tempo e duração em Go. No entanto, algumas partes do código estão faltando. Sua tarefa é completar o código para fazê-lo funcionar como esperado.

- Conhecimento básico da linguagem de programação Go.
- Familiaridade com o suporte de tempo e duração do Go.

```sh
$ go run time.go
2012-10-31 15:50:13.793654 +0000 UTC
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
25891h15m15.142266763s
25891.25420618521
1.5534752523711128e+06
9.320851514226677e+07
93208515142266763
2012-10-31 15:50:13.793654 +0000 UTC
2006-12-05 01:19:43.509120474 +0000 UTC

# Em seguida, vamos analisar a ideia relacionada de tempo em relação à
# época Unix (Unix epoch).
```

Aqui está o código completo:

```go
// Go oferece suporte extensivo para tempos e durações;
// aqui estão alguns exemplos.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Começaremos obtendo o tempo atual.
	now := time.Now()
	p(now)

	// Você pode construir uma struct `time` fornecendo o
	// ano, mês, dia, etc. Os tempos estão sempre associados
	// a uma `Location`, ou seja, fuso horário.
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	// Você pode extrair os vários componentes do valor do tempo
	// como esperado.
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	// O `Weekday` de segunda a domingo também está disponível.
	p(then.Weekday())

	// Esses métodos comparam dois tempos, testando se o
	// primeiro ocorre antes, depois ou ao mesmo tempo
	// que o segundo, respectivamente.
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// O método `Sub` retorna um `Duration` representando
	// o intervalo entre dois tempos.
	diff := now.Sub(then)
	p(diff)

	// Podemos calcular a duração em
	// várias unidades.
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// Você pode usar `Add` para avançar um tempo por uma determinada
	// duração, ou com um `-` para retroceder por uma
	// duração.
	p(then.Add(diff))
	p(then.Add(-diff))
}
```
