# Escrevendo Arquivos

Você precisa escrever um programa Go que escreva uma string e bytes em um arquivo e use _buffered writers_ (escritores com buffer).

- O programa deve escrever uma string e bytes em um arquivo.
- O programa deve usar _buffered writers_ (escritores com buffer).

```sh
# Tente executar o código de escrita de arquivos.
$ go run writing-files.go
wrote 5 bytes
wrote 7 bytes
wrote 9 bytes

# Em seguida, verifique o conteúdo dos arquivos escritos.
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# Em seguida, veremos como aplicar algumas das ideias de I/O de arquivos
# que acabamos de ver aos fluxos `stdin` e `stdout`.
```

A seguir, o código completo:

```go
// Escrever arquivos em Go segue padrões semelhantes aos
// que vimos anteriormente para leitura.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	// Para começar, aqui está como despejar uma string (ou apenas
	// bytes) em um arquivo.
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// Para gravações mais granulares, abra um arquivo para escrita.
	f, err := os.Create("/tmp/dat2")
	check(err)

	// É idiomático adiar um `Close` imediatamente
	// após abrir um arquivo.
	defer f.Close()

	// Você pode `Write` fatias de bytes como esperado.
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("wrote %d bytes\n", n2)

	// Um `WriteString` também está disponível.
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n3)

	// Emita um `Sync` para descarregar as gravações no armazenamento estável.
	f.Sync()

	// `bufio` fornece *buffered writers* (escritores com buffer) além
	// dos *buffered readers* (leitores com buffer) que vimos anteriormente.
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n4)

	// Use `Flush` para garantir que todas as operações em buffer tenham
	// sido aplicadas ao escritor subjacente.
	w.Flush()

}
```
