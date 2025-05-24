# Defer (Adiar)

Neste laboratório, você precisa usar `defer` para criar um arquivo, escrever nele e, em seguida, fechá-lo quando terminar.

- A função `createFile` deve criar um arquivo com o caminho fornecido e retornar um ponteiro para o arquivo.
- A função `writeFile` deve escrever a string "data" no arquivo.
- A função `closeFile` deve fechar o arquivo e verificar se há erros.

```sh
# Executar o programa confirma que o arquivo é fechado
# após ser escrito.
$ go run defer.go
creating
writing
closing
```

Aqui está o código completo:

```go
// _Defer_ é usado para garantir que uma chamada de função seja
// executada mais tarde na execução de um programa, geralmente para
// fins de limpeza. `defer` é frequentemente usado onde, por exemplo,
// `ensure` e `finally` seriam usados em outras linguagens.

package main

import (
	"fmt"
	"os"
)

// Suponha que quiséssemos criar um arquivo, escrever nele,
// e então fechá-lo quando terminarmos. Veja como poderíamos
// fazer isso com `defer`.
func main() {

	// Imediatamente após obter um objeto de arquivo com
	// `createFile`, adiamos o fechamento desse arquivo
	// com `closeFile`. Isso será executado no final
	// da função que o contém (`main`), após
	// `writeFile` ter terminado.
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err != nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprintln(f, "data")

}

func closeFile(f *os.File) {
	fmt.Println("closing")
	err := f.Close()
	// É importante verificar se há erros ao fechar um
	// arquivo, mesmo em uma função adiada.
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}
```
