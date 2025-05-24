# Diretiva Embed

Sua tarefa é modificar o código fornecido para incorporar arquivos e pastas no binário Go e imprimir seus conteúdos.

- Você deve usar o pacote `embed` para incorporar arquivos e pastas.
- Você deve usar os tipos `string` e `[]byte` para armazenar o conteúdo dos arquivos incorporados.
- Você deve usar o tipo `embed.FS` para incorporar múltiplos arquivos ou pastas com curingas (wildcards).
- Você deve imprimir o conteúdo dos arquivos incorporados.

```sh
# Use estes comandos para executar o exemplo.
# (Nota: devido à limitação no go playground,
# este exemplo só pode ser executado em sua máquina local.)
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```

Aqui está o código completo:

```go
// `//go:embed` é uma [diretiva do compilador](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives) que
// permite que programas incluam arquivos e pastas arbitrários no binário Go no
// momento da compilação (build time). Leia mais sobre a diretiva embed
// [aqui](https://pkg.go.dev/embed).
package main

// Importe o pacote `embed`; se você não usar nenhum identificador exportado
// deste pacote, você pode fazer uma importação em branco com `_ "embed"`.
import (
	"embed"
)

// Diretivas `embed` aceitam caminhos relativos ao diretório que contém o
// arquivo fonte Go. Esta diretiva incorpora o conteúdo do arquivo na
// variável `string` imediatamente após ela.
//
//go:embed folder/single_file.txt
var fileString string

// Ou incorpore o conteúdo do arquivo em um `[]byte`.
//
//go:embed folder/single_file.txt
var fileByte []byte

// Também podemos incorporar múltiplos arquivos ou até mesmo pastas com curingas.
// Isso usa uma variável do [tipo embed.FS](https://pkg.go.dev/embed#FS), que
// implementa um sistema de arquivos virtual simples.
//
//go:embed folder/single_file.txt
//go:embed folder/*.hash
var folder embed.FS

func main() {

	// Imprime o conteúdo de `single_file.txt`.
	print(fileString)
	print(string(fileByte))

	// Recupera alguns arquivos da pasta incorporada.
	content1, _ := folder.ReadFile("folder/file1.hash")
	print(string(content1))

	content2, _ := folder.ReadFile("folder/file2.hash")
	print(string(content2))
}
```
