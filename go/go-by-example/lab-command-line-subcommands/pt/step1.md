# Subcomandos da Linha de Comando

Você deve criar um programa que suporte dois subcomandos, `foo` e `bar`, cada um com seu próprio conjunto de flags (bandeiras). O subcomando `foo` deve ter duas flags, `enable` e `name`, enquanto o subcomando `bar` deve ter uma flag, `level`.

- O programa deve usar o pacote `flag` para definir e analisar as flags.
- O subcomando `foo` deve ter duas flags, `enable` e `name`, ambas do tipo string.
- O subcomando `bar` deve ter uma flag, `level`, do tipo int.
- O programa deve imprimir uma mensagem de erro se um subcomando inválido for fornecido.
- O programa deve imprimir os valores das flags para o subcomando que for invocado.

```sh
$ go build command-line-subcommands.go

# Primeiro, invoque o subcomando foo.
$ ./command-line-subcommands foo -enable -name=joe a1 a2
subcommand 'foo'
enable: true
name: joe
tail: [a1 a2]

# Agora tente bar.
$ ./command-line-subcommands bar -level 8 a1
subcommand 'bar'
level: 8
tail: [a1]

# Mas bar não aceitará as flags de foo.
$ ./command-line-subcommands bar -enable a1
flag provided but not defined: -enable
Usage of bar:
-level int
level

# Em seguida, vamos analisar as variáveis de ambiente, outra forma comum
# de parametrizar programas.
```

Aqui está o código completo:

```go
// Algumas ferramentas de linha de comando, como a ferramenta `go` ou `git`
// têm muitos *subcomandos*, cada um com seu próprio conjunto de
// flags. Por exemplo, `go build` e `go get` são dois
// subcomandos diferentes da ferramenta `go`.
// O pacote `flag` nos permite definir facilmente
// subcomandos simples que têm suas próprias flags.

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// Declaramos um subcomando usando a função `NewFlagSet`
	// e prosseguimos para definir novas flags específicas
	// para este subcomando.
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "enable")
	fooName := fooCmd.String("name", "", "name")

	// Para um subcomando diferente, podemos definir diferentes
	// flags suportadas.
	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "level")

	// O subcomando é esperado como o primeiro argumento
	// para o programa.
	if len(os.Args) < 2 {
		fmt.Println("expected 'foo' or 'bar' subcommands")
		os.Exit(1)
	}

	// Verifique qual subcomando é invocado.
	switch os.Args[1] {

	// Para cada subcomando, analisamos suas próprias flags e
	// temos acesso aos argumentos posicionais restantes.
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("subcommand 'foo'")
		fmt.Println("  enable:", *fooEnable)
		fmt.Println("  name:", *fooName)
		fmt.Println("  tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("subcommand 'bar'")
		fmt.Println("  level:", *barLevel)
		fmt.Println("  tail:", barCmd.Args())
	default:
		fmt.Println("expected 'foo' or 'bar' subcommands")
		os.Exit(1)
	}
}
```
