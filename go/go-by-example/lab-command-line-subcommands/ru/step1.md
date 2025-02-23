# Командная строка: подкоманды

Требуется создать программу, которая поддерживает две подкоманды: `foo` и `bar`, каждая с собственной группой флагов. Подкоманда `foo` должна иметь два флага: `enable` и `name`, а подкоманда `bar` должна иметь один флаг: `level`.

- Программа должна использовать пакет `flag` для определения и разбора флагов.
- Подкоманда `foo` должна иметь два флага `enable` и `name`, оба типа `string`.
- Подкоманда `bar` должна иметь один флаг `level` типа `int`.
- Программа должна выводить сообщение об ошибке, если указана недействительная подкоманда.
- Программа должна выводить значения флагов для вызванной подкоманды.

```sh
$ go build command-line-subcommands.go

# Сначала вызовем подкоманду foo.
$./command-line-subcommands foo -enable -name=joe a1 a2
подкоманда 'foo'
enable: true
name: joe
tail: [a1 a2]

# Теперь попробуем bar.
$./command-line-subcommands bar -level 8 a1
подкоманда 'bar'
level: 8
tail: [a1]

# Но bar не примет флаги foo.
$./command-line-subcommands bar -enable a1
флаг указан, но не определён: -enable
Usage of bar:
-level int
уровень

# Далее мы рассмотрим переменные окружения, другой распространённый
# способ параметризации программ.
```

Ниже представлен полный код:

```go
// Некоторые инструменты командной строки, такие как `go` или `git`,
// имеют множество *подкоманд*, каждая с собственной группой
// флагов. Например, `go build` и `go get` - это две
// разные подкоманды инструмента `go`.
// Пакет `flag` позволяет легко определить простые
// подкоманды с собственными флагами.

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// Мы объявляем подкоманду с использованием функции `NewFlagSet`,
	// а затем определяем новые флаги, специфичные для этой подкоманды.
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "enable")
	fooName := fooCmd.String("name", "", "name")

	// Для другой подкоманды мы можем определить другие
	// поддерживаемые флаги.
	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "level")

	// Подкоманда ожидается в качестве первого аргумента
	// к программе.
	if len(os.Args) < 2 {
		fmt.Println("ожидаются подкоманды 'foo' или 'bar'")
		os.Exit(1)
	}

	// Проверяем, какая подкоманда вызвана.
	switch os.Args[1] {

	// Для каждой подкоманды мы разбираем свои флаги и
	// имеем доступ к последующим позиционным аргументам.
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("подкоманда 'foo'")
		fmt.Println("  enable:", *fooEnable)
		fmt.Println("  name:", *fooName)
		fmt.Println("  tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("подкоманда 'bar'")
		fmt.Println("  level:", *barLevel)
		fmt.Println("  tail:", barCmd.Args())
	default:
		fmt.Println("ожидаются подкоманды 'foo' или 'bar'")
		os.Exit(1)
	}
}

```
