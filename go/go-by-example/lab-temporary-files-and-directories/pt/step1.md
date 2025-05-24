# Arquivos e Diretórios Temporários

Neste laboratório, você precisa criar arquivos e diretórios temporários em Go.

- Use `os.CreateTemp` para criar um arquivo temporário.
- Use `os.MkdirTemp` para criar um diretório temporário.
- Use `os.RemoveAll` para remover o diretório temporário.
- Use `os.WriteFile` para escrever dados em um arquivo.

```sh
$ go run temporary-files-and-directories.go
Temp file name: /tmp/sample610887201
Temp dir name: /tmp/sampledir898854668
```

A seguir, o código completo:

```go
// Ao longo da execução do programa, frequentemente queremos criar
// dados que não são necessários após a saída do programa.
// *Arquivos e diretórios temporários* são úteis para este
// propósito, pois não poluem o sistema de arquivos ao longo do
// tempo.

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

	// A maneira mais fácil de criar um arquivo temporário é
	// chamando `os.CreateTemp`. Ele cria um arquivo *e*
	// o abre para leitura e escrita. Fornecemos `""`
	// como o primeiro argumento, então `os.CreateTemp` irá
	// criar o arquivo no local padrão para o nosso sistema operacional.
	f, err := os.CreateTemp("", "sample")
	check(err)

	// Exibe o nome do arquivo temporário. Em
	// sistemas operacionais baseados em Unix, o diretório provavelmente será `/tmp`.
	// O nome do arquivo começa com o prefixo fornecido como o
	// segundo argumento para `os.CreateTemp` e o restante
	// é escolhido automaticamente para garantir que chamadas
	// concorrentes sempre criem nomes de arquivos diferentes.
	fmt.Println("Temp file name:", f.Name())

	// Limpe o arquivo depois de terminarmos. O sistema operacional é
	// propenso a limpar arquivos temporários por conta própria após
	// algum tempo, mas é uma boa prática fazer isso
	// explicitamente.
	defer os.Remove(f.Name())

	// Podemos escrever alguns dados no arquivo.
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	// Se pretendemos escrever muitos arquivos temporários, podemos
	// preferir criar um *diretório* temporário.
	// Os argumentos de `os.MkdirTemp` são os mesmos que os de
	// `CreateTemp`, mas ele retorna um *nome* de diretório
	// em vez de um arquivo aberto.
	dname, err := os.MkdirTemp("", "sampledir")
	check(err)
	fmt.Println("Temp dir name:", dname)

	defer os.RemoveAll(dname)

	// Agora podemos sintetizar nomes de arquivos temporários
	// prefixando-os com nosso diretório temporário.
	fname := filepath.Join(dname, "file1")
	err = os.WriteFile(fname, []byte{1, 2}, 0666)
	check(err)
}
```
