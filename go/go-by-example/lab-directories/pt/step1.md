# Diretórios

Crie um programa Go que cria um novo subdiretório no diretório de trabalho atual, cria uma hierarquia de diretórios, incluindo os pais, lista o conteúdo do diretório, altera o diretório de trabalho atual e visita um diretório recursivamente.

- Crie um novo subdiretório no diretório de trabalho atual.
- Ao criar diretórios temporários, é uma boa prática usar `defer` para removê-los. `os.RemoveAll` irá deletar toda uma árvore de diretórios (semelhante a `rm -rf`).
- Crie uma hierarquia de diretórios, incluindo os pais, com `MkdirAll`. Isso é semelhante ao comando de linha de comando `mkdir -p`.
- `ReadDir` lista o conteúdo do diretório, retornando uma fatia de objetos `os.DirEntry`.
- `Chdir` nos permite alterar o diretório de trabalho atual, semelhante a `cd`.
- Visite um diretório recursivamente, incluindo todos os seus subdiretórios. `Walk` aceita uma função de callback para lidar com cada arquivo ou diretório visitado.

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

Aqui está o código completo:

```go
// Go tem várias funções úteis para trabalhar com
// *diretórios* no sistema de arquivos.

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	// Crie um novo subdiretório no diretório de trabalho
	// atual.
	err := os.Mkdir("subdir", 0755)
	check(err)

	// Ao criar diretórios temporários, é uma boa
	// prática usar `defer` para removê-los. `os.RemoveAll`
	// irá deletar toda uma árvore de diretórios (semelhante a
	// `rm -rf`).
	defer os.RemoveAll("subdir")

	// Função auxiliar para criar um novo arquivo vazio.
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// Podemos criar uma hierarquia de diretórios, incluindo
	// os pais, com `MkdirAll`. Isso é semelhante ao
	// comando de linha de comando `mkdir -p`.
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` lista o conteúdo do diretório, retornando uma
	// fatia de objetos `os.DirEntry`.
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` nos permite alterar o diretório de trabalho,
	// semelhante a `cd`.
	err = os.Chdir("subdir/parent/child")
	check(err)

	// Agora veremos o conteúdo de `subdir/parent/child`
	// ao listar o diretório *atual*.
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `cd` de volta para onde começamos.
	err = os.Chdir("../../..")
	check(err)

	// Também podemos visitar um diretório *recursivamente*,
	// incluindo todos os seus subdiretórios. `Walk` aceita
	// uma função de callback para lidar com cada arquivo ou
	// diretório visitado.
	fmt.Println("Visiting subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` é chamado para cada arquivo ou diretório encontrado
// recursivamente por `filepath.Walk`.
func visit(p string, info os.FileInfo, err error) error {
	if err != nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}
```
