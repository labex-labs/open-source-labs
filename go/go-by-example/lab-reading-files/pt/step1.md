# Lendo Arquivos (Reading Files)

Você precisa ler arquivos em seu programa Go e realizar diferentes operações nos dados do arquivo.

- Você deve estar familiarizado com os conceitos básicos de programação Go.
- Você deve ter o Go instalado em seu computador.

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# Em seguida, veremos como escrever arquivos.
```

Aqui está o código completo:

```go
// Ler e escrever arquivos são tarefas básicas necessárias para
// muitos programas Go. Primeiro, veremos alguns exemplos de
// leitura de arquivos.

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// Ler arquivos requer verificar a maioria das chamadas em busca de erros.
// Este auxiliar simplificará nossas verificações de erros abaixo.
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	// Talvez a tarefa mais básica de leitura de arquivos seja
	// absorver todo o conteúdo de um arquivo na memória.
	dat, err := os.ReadFile("/tmp/dat")
	check(err)
	fmt.Print(string(dat))

	// Você frequentemente desejará ter mais controle sobre como e quais
	// partes de um arquivo são lidas. Para essas tarefas, comece
	// abrindo um arquivo com `Open` para obter um valor `os.File`.
	f, err := os.Open("/tmp/dat")
	check(err)

	// Leia alguns bytes do início do arquivo.
	// Permita que até 5 sejam lidos, mas observe também quantos
	// foram realmente lidos.
	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)
	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// Você também pode `Seek` para uma localização conhecida no arquivo
	// e `Read` a partir daí.
	o2, err := f.Seek(6, 0)
	check(err)
	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: ", n2, o2)
	fmt.Printf("%v\n", string(b2[:n2]))

	// O pacote `io` fornece algumas funções que podem
	// ser úteis para a leitura de arquivos. Por exemplo, leituras
	// como as acima podem ser implementadas de forma mais robusta
	// com `ReadAtLeast`.
	o3, err := f.Seek(6, 0)
	check(err)
	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// Não há retrocesso (rewind) embutido, mas `Seek(0, 0)`
	// realiza isso.
	_, err = f.Seek(0, 0)
	check(err)

	// O pacote `bufio` implementa um leitor com buffer
	// que pode ser útil tanto por sua eficiência
	// com muitas leituras pequenas quanto por causa dos métodos de leitura
	// adicionais que ele fornece.
	r4 := bufio.NewReader(f)
	b4, err := r4.Peek(5)
	check(err)
	fmt.Printf("5 bytes: %s\n", string(b4))

	// Feche o arquivo quando terminar (geralmente isso seria
	// agendado imediatamente após `Open` com
	// `defer`).
	f.Close()
}
```
