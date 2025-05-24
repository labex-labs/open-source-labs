# Caminhos de Arquivos

Neste laboratório, você precisa usar o pacote `filepath` para realizar várias operações em caminhos de arquivos, como construir caminhos de forma portátil, dividir um caminho em componentes de diretório e arquivo, verificar se um caminho é absoluto, encontrar a extensão de um arquivo e encontrar um caminho relativo entre dois caminhos.

- Use `Join` para construir caminhos de forma portátil.
- Use `Dir` e `Base` para dividir um caminho em componentes de diretório e arquivo.
- Use `IsAbs` para verificar se um caminho é absoluto.
- Use `Ext` para encontrar a extensão de um arquivo.
- Use `TrimSuffix` para remover a extensão de um nome de arquivo.
- Use `Rel` para encontrar um caminho relativo entre dois caminhos.

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```

Aqui está o código completo:

```go
// O pacote `filepath` fornece funções para analisar
// e construir *caminhos de arquivos* de forma portátil
// entre sistemas operacionais; `dir/file` no Linux vs.
// `dir\file` no Windows, por exemplo.
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	// `Join` deve ser usado para construir caminhos de forma
	// portátil. Ele recebe qualquer número de argumentos
	// e constrói um caminho hierárquico a partir deles.
	p := filepath.Join("dir1", "dir2", "filename")
	fmt.Println("p:", p)

	// Você sempre deve usar `Join` em vez de
	// concatenar `/`s ou `\`s manualmente. Além de
	// fornecer portabilidade, `Join` também
	// normalizará os caminhos removendo separadores
	// supérfluos e mudanças de diretório.
	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// `Dir` e `Base` podem ser usados para dividir um caminho em
	// o diretório e o arquivo. Alternativamente, `Split` irá
	// retornar ambos na mesma chamada.
	fmt.Println("Dir(p):", filepath.Dir(p))
	fmt.Println("Base(p):", filepath.Base(p))

	// Podemos verificar se um caminho é absoluto.
	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	filename := "config.json"

	// Alguns nomes de arquivos têm extensões após um ponto. Nós
	// podemos separar a extensão desses nomes com `Ext`.
	ext := filepath.Ext(filename)
	fmt.Println(ext)

	// Para encontrar o nome do arquivo com a extensão removida,
	// use `strings.TrimSuffix`.
	fmt.Println(strings.TrimSuffix(filename, ext))

	// `Rel` encontra um caminho relativo entre uma *base* e um
	// *alvo*. Ele retorna um erro se o alvo não puder
	// ser tornado relativo à base.
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err != nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/t/file")
	if err != nil {
		panic(err)
	}
	fmt.Println(rel)
}
```
