# Flags de linha de comando

Implemente um programa Golang que analisa flags de linha de comando e produz as opções analisadas e quaisquer argumentos posicionais restantes. O programa deve suportar as seguintes flags:

- `word`: uma flag string com um valor padrão de `"foo"`.
- `numb`: uma flag inteira com um valor padrão de `42`.
- `fork`: uma flag booleana com um valor padrão de `false`.
- `svar`: uma flag string que usa uma variável existente declarada em outro lugar no programa.

- O programa deve usar o pacote `flag` para analisar as flags de linha de comando.
- O programa deve produzir as opções analisadas e quaisquer argumentos posicionais restantes.
- O programa deve suportar as flags `word`, `numb`, `fork` e `svar` conforme descrito acima.

```sh
# Para experimentar com o programa de flags de linha de comando, é
# melhor primeiro compilá-lo e, em seguida, executar o
# binário resultante diretamente.
$ go build command-line-flags.go

# Experimente o programa construído, primeiro fornecendo valores para
# todas as flags.
$ ./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# Observe que, se você omitir flags, elas assumirão automaticamente
# seus valores padrão.
$ ./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# Argumentos posicionais restantes podem ser fornecidos após
# quaisquer flags.
$ ./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# Observe que o pacote `flag` requer que todas as flags
# apareçam antes dos argumentos posicionais (caso contrário, as flags
# serão interpretadas como argumentos posicionais).
$ ./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# Use as flags `-h` ou `--help` para obter ajuda gerada
# automaticamente para o programa de linha de comando.
$ ./command-line-flags -h
Usage of ./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# Se você fornecer uma flag que não foi especificada para o
# pacote `flag`, o programa imprimirá uma mensagem de erro
# e mostrará o texto de ajuda novamente.
$ ./command-line-flags -wat
flag provided but not defined: -wat
Usage of ./command-line-flags:
...
```

Aqui está o código completo:

```go
// [_Flags de linha de comando_](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option)
// são uma forma comum de especificar opções para programas de
// linha de comando. Por exemplo, em `wc -l`, o `-l` é uma
// flag de linha de comando.

package main

// Go fornece um pacote `flag` que suporta a análise básica de
// flags de linha de comando. Usaremos este pacote para
// implementar nosso exemplo de programa de linha de comando.
import (
	"flag"
	"fmt"
)

func main() {

	// Declarações básicas de flag estão disponíveis para opções string,
	// inteiras e booleanas. Aqui declaramos uma
	// flag string `word` com um valor padrão `"foo"`
	// e uma breve descrição. Esta função `flag.String`
	// retorna um ponteiro string (não um valor string);
	// veremos como usar este ponteiro abaixo.
	wordPtr := flag.String("word", "foo", "a string")

	// Isso declara as flags `numb` e `fork`, usando uma
	// abordagem semelhante à flag `word`.
	numbPtr := flag.Int("numb", 42, "an int")
	forkPtr := flag.Bool("fork", false, "a bool")

	// Também é possível declarar uma opção que usa uma
	// variável existente declarada em outro lugar no programa.
	// Observe que precisamos passar um ponteiro para a
	// função de declaração da flag.
	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	// Depois que todas as flags forem declaradas, chame `flag.Parse()`
	// para executar a análise da linha de comando.
	flag.Parse()

	// Aqui, apenas exibiremos as opções analisadas e
	// quaisquer argumentos posicionais restantes. Observe que
	// precisamos desreferenciar os ponteiros com, por exemplo, `*wordPtr`
	// para obter os valores reais das opções.
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}
```
