# Executando Processos

O problema é substituir o processo Go atual por outro processo, como um processo que não seja Go.

- Linguagem de programação Go
- Conhecimento básico da função `exec` do Go
- Familiaridade com variáveis de ambiente

```sh
# Quando executamos nosso programa, ele é substituído por `ls`.
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29 .
drwxr-xr-x 91 mark 3.0K Oct 3 12:50 ..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# Observe que Go não oferece um `fork` Unix clássico
# função. Normalmente, isso não é um problema, pois
# iniciar goroutines, gerar processos e executar
# processos cobre a maioria dos casos de uso para `fork`.
```

A seguir, o código completo:

```go
// No exemplo anterior, analisamos
// [gerando processos externos](spawning-processes). Nós
// fazemos isso quando precisamos de um processo externo acessível a
// um processo Go em execução. Às vezes, só queremos
// substituir completamente o processo Go atual por outro
// (talvez não Go). Para fazer isso, usaremos o Go
// implementação da função clássica
// <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>
// função.

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// Para nosso exemplo, executaremos `ls`. Go requer um
	// caminho absoluto para o binário que queremos executar, então
	// usaremos `exec.LookPath` para encontrá-lo (provavelmente
	// `/bin/ls`).
	binary, lookErr := exec.LookPath("ls")
	if lookErr != nil {
		panic(lookErr)
	}

	// `Exec` requer argumentos em forma de slice (em
	// oposição a uma grande string). Daremos a `ls` alguns
	// argumentos comuns. Observe que o primeiro argumento deve
	// ser o nome do programa.
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` também precisa de um conjunto de [variáveis de ambiente](environment-variables)
	// para usar. Aqui, apenas fornecemos nosso atual
	// ambiente.
	env := os.Environ()

	// Aqui está a chamada `syscall.Exec` real. Se esta chamada for
	// bem-sucedida, a execução do nosso processo terminará
	// aqui e será substituído pelo processo `/bin/ls -a -l -h`
	// processo. Se houver um erro, receberemos um retorno
	// valor.
	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}
```
