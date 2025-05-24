# Testes e Benchmarking

O problema a ser resolvido neste laboratório é testar e fazer benchmarking de uma implementação simples de uma função de mínimo inteiro chamada `IntMin`.

- O pacote `testing` deve ser importado.
- A função `IntMin` deve receber dois parâmetros inteiros e retornar um inteiro.
- A função `TestIntMinBasic` deve testar a função `IntMin` para valores de entrada básicos.
- A função `TestIntMinTableDriven` deve testar a função `IntMin` usando um estilo baseado em tabela.
- A função `BenchmarkIntMin` deve fazer benchmarking da função `IntMin`.

```sh
# Executar todos os testes no projeto atual em modo verbose.

# Executar todos os benchmarks no projeto atual. Todos os testes
# são executados antes dos benchmarks. A flag `bench` filtra
# nomes de funções de benchmark com uma regexp.
```

Aqui está o código completo:

```go
// Testes unitários são uma parte importante da escrita de
// programas Go com princípios. O pacote `testing`
// fornece as ferramentas que precisamos para escrever testes unitários
// e o comando `go test` executa os testes.

// Para fins de demonstração, este código está no pacote
// `main`, mas poderia ser qualquer pacote. O código de teste
// normalmente reside no mesmo pacote que o código que ele testa.
package main

import (
	"fmt"
	"testing"
)

// Estaremos testando esta implementação simples de um
// mínimo inteiro. Tipicamente, o código que estamos testando
// estaria em um arquivo fonte chamado algo como
// `intutils.go`, e o arquivo de teste para ele seria então
// chamado `intutils_test.go`.
func IntMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Um teste é criado escrevendo uma função com um nome
// começando com `Test`.
func TestIntMinBasic(t *testing.T) {
	ans := IntMin(2, -2)
	if ans != -2 {
		// `t.Error*` relatará falhas nos testes, mas continuará
		// executando o teste. `t.Fatal*` relatará falhas nos testes
		// e interromperá o teste imediatamente.
		t.Errorf("IntMin(2, -2) = %d; want -2", ans)
	}
}

// Escrever testes pode ser repetitivo, então é idiomático
// usar um *estilo baseado em tabela*, onde as entradas de teste e
// as saídas esperadas são listadas em uma tabela e um único loop
// percorre-as e executa a lógica do teste.
func TestIntMinTableDriven(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{0, -1, -1},
		{-1, 0, -1},
	}

	for _, tt := range tests {
		// t.Run permite executar "subtestes", um para cada
		// entrada da tabela. Estes são mostrados separadamente
		// ao executar `go test -v`.
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := IntMin(tt.a, tt.b)
			if ans != tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

// Testes de benchmark normalmente vão em arquivos `_test.go` e são
// nomeados começando com `Benchmark`. O executor `testing`
// executa cada função de benchmark várias vezes, aumentando
// `b.N` em cada execução até que colete uma medição precisa.
func BenchmarkIntMin(b *testing.B) {
	// Tipicamente, o benchmark executa uma função que estamos
	// fazendo benchmarking em um loop `b.N` vezes.
	for i := 0; i < b.N; i++ {
		IntMin(1, 2)
	}
}
```
