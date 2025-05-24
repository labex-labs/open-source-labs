# Números Aleatórios

Você deve escrever um programa que gera inteiros e floats aleatórios dentro de um intervalo especificado. O programa também deve ser capaz de produzir sequências variadas de números, alterando a semente (seed).

- O programa deve usar o pacote `math/rand` para gerar números aleatórios.
- O programa deve gerar inteiros aleatórios dentro de um intervalo especificado.
- O programa deve gerar floats aleatórios dentro de um intervalo especificado.
- O programa deve ser capaz de produzir sequências variadas de números, alterando a semente.

```sh
# Dependendo de onde você executar este exemplo, alguns dos
# números gerados podem ser diferentes. Observe que no
# Go playground, a semente com `time.Now()` ainda
# produz resultados determinísticos devido à forma como o
# playground é implementado.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Consulte a documentação do pacote [`math/rand`](https://pkg.go.dev/math/rand)
# para obter referências sobre outras quantidades aleatórias
# que o Go pode fornecer.
```

Aqui está o código completo:

```go
// O pacote `math/rand` do Go fornece
// geração de [números pseudorrandômicos](https://en.wikipedia.org/wiki/Pseudorandom_number_generator).

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	// Por exemplo, `rand.Intn` retorna um `int` aleatório n,
	// `0 <= n < 100`.
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` retorna um `float64` `f`,
	// `0.0 <= f < 1.0`.
	fmt.Println(rand.Float64())

	// Isso pode ser usado para gerar floats aleatórios em
	// outros intervalos, por exemplo, `5.0 <= f' < 10.0`.
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// O gerador de números padrão é determinístico, então ele
	// produzirá a mesma sequência de números toda vez por padrão.
	// Para produzir sequências variadas, forneça a ele uma semente que muda.
	// Observe que isso não é seguro para usar para números aleatórios que você
	// pretende manter em segredo; use `crypto/rand` para esses.
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// Chame o `rand.Rand` resultante assim como as
	// funções no pacote `rand`.
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// Se você semear uma fonte com o mesmo número, ela
	// produz a mesma sequência de números aleatórios.
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
	s3 := rand.NewSource(42)
	r3 := rand.New(s3)
	fmt.Print(r3.Intn(100), ",")
	fmt.Print(r3.Intn(100))
}
```
