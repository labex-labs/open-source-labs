# Recover (Recuperação)

A função `mayPanic` no código fornecido irá entrar em `panic` quando chamada. Sua tarefa é modificar a função `main` para recuperar do `panic` e imprimir a mensagem de erro.

- Use a função `recover` para lidar com o `panic` na função `mayPanic`.
- Imprima a mensagem de erro quando um `panic` ocorrer.

```sh
$ go run recover.go
Recovered. Error:
a problem
```

Aqui está o código completo:

```go
// Go torna possível _recuperar_ de um panic, usando
// a função embutida `recover`. Um `recover` pode
// impedir que um `panic` interrompa o programa e permitir que ele
// continue com a execução.

// Um exemplo de onde isso pode ser útil: um servidor
// não gostaria de travar se uma das conexões do cliente
// apresentar um erro crítico. Em vez disso, o servidor
// gostaria de fechar essa conexão e continuar servindo
// outros clientes. Na verdade, isso é o que o `net/http` do Go
// faz por padrão para servidores HTTP.

package main

import "fmt"

// Esta função entra em panic.
func mayPanic() {
	panic("a problem")
}

func main() {
	// `recover` deve ser chamado dentro de uma função adiada (deferred).
	// Quando a função que o envolve entra em panic, o defer irá
	// ativar e uma chamada `recover` dentro dele irá capturar
	// o panic.
	defer func() {
		if r := recover(); r != nil {
			// O valor de retorno de `recover` é o erro levantado na
			// chamada para `panic`.
			fmt.Println("Recovered. Error:\n", r)
		}
	}()

	mayPanic()

	// Este código não será executado, porque `mayPanic` entra em panic.
	// A execução de `main` para no ponto do
	// panic e retoma no closure adiado.
	fmt.Println("After mayPanic()")
}
```
