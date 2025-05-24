# Formatação e Análise de Tempo

O problema é formatar e analisar tempo em Golang usando os layouts fornecidos.

- Use o pacote `time` para formatar e analisar tempo.
- Use o layout `time.RFC3339` para formatar e analisar tempo.
- Use o tempo de referência `Mon Jan 2 15:04:05 MST 2006` para mostrar o padrão com o qual formatar/analisar um determinado tempo/string.
- Use a função `Parse` para analisar tempo.
- Use a função `Format` para formatar tempo.
- Use a função `fmt.Println` para imprimir o tempo formatado.
- Use a função `fmt.Printf` para imprimir o tempo formatado com componentes extraídos.

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006": ...
```

Aqui está o código completo:

```go
// Go suporta formatação e análise de tempo via
// layouts baseados em padrões.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Aqui está um exemplo básico de formatação de um tempo
	// de acordo com RFC3339, usando a constante de layout
	// correspondente.
	t := time.Now()
	p(t.Format(time.RFC3339))

	// A análise de tempo usa os mesmos valores de layout que `Format`.
	t1, e := time.Parse(
		time.RFC3339,
		"2012-11-01T22:08:41+00:00")
	p(t1)

	// `Format` e `Parse` usam layouts baseados em exemplos. Normalmente
	// você usará uma constante de `time` para esses layouts, mas
	// você também pode fornecer layouts personalizados. Os layouts devem usar o
	// tempo de referência `Mon Jan 2 15:04:05 MST 2006` para mostrar o
	// padrão com o qual formatar/analisar um determinado tempo/string.
	// O tempo de exemplo deve ser exatamente como mostrado: o ano 2006,
	// 15 para a hora, segunda-feira para o dia da semana, etc.
	p(t.Format("3:04PM"))
	p(t.Format("Mon Jan _2 15:04:05 2006"))
	p(t.Format("2006-01-02T15:04:05.999999-07:00"))
	form := "3 04 PM"
	t2, e := time.Parse(form, "8 41 PM")
	p(t2)

	// Para representações puramente numéricas, você também pode
	// usar formatação de string padrão com os
	// componentes extraídos do valor do tempo.
	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())

	// `Parse` retornará um erro na entrada malformada
	// explicando o problema de análise.
	ansic := "Mon Jan _2 15:04:05 2006"
	_, e = time.Parse(ansic, "8:41PM")
	p(e)
}
```
