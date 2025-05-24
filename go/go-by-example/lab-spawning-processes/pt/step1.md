# Geração de Processos (Spawning Processes)

O laboratório requer a implementação de um programa Go que gera processos externos e coleta sua saída.

- O programa deve ser capaz de gerar processos externos.
- O programa deve ser capaz de coletar a saída dos processos externos.
- O programa deve lidar com erros que podem surgir durante a execução dos processos externos.

```sh
# Os programas gerados retornam a saída que é a mesma
# como se os tivéssemos executado diretamente da linha de comando.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date não tem uma flag `-x`, então ele sairá com
# uma mensagem de erro e código de retorno diferente de zero.
command exited with rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29 .
drwxr-xr-x 91 mark 3.0K Oct 3 12:50 ..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```

Aqui está o código completo:

```go
// Às vezes, nossos programas Go precisam gerar outros processos, não-Go.

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {

	// Começaremos com um comando simples que não recebe
	// argumentos ou entrada e apenas imprime algo para
	// stdout. O auxiliar `exec.Command` cria um objeto
	// para representar este processo externo.
	dateCmd := exec.Command("date")

	// O método `Output` executa o comando, espera que ele
	// termine e coleta sua saída padrão.
	// Se não houver erros, `dateOut` conterá bytes
	// com as informações da data.
	dateOut, err := dateCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// `Output` e outros métodos de `Command` retornarão
	// `*exec.Error` se houver um problema ao executar o
	// comando (por exemplo, caminho errado), e `*exec.ExitError`
	// se o comando foi executado, mas saiu com um retorno diferente de zero
	// código.
	_, err = exec.Command("date", "-x").Output()
	if err != nil {
		switch e := err.(type) {
		case *exec.Error:
			fmt.Println("failed executing:", err)
		case *exec.ExitError:
			fmt.Println("command exit rc =", e.ExitCode())
		default:
			panic(err)
		}
	}

	// Em seguida, veremos um caso um pouco mais complexo
	// onde canalizamos dados para o processo externo em seu
	// `stdin` e coletamos os resultados de seu `stdout`.
	grepCmd := exec.Command("grep", "hello")

	// Aqui, pegamos explicitamente os pipes de entrada/saída, iniciamos
	// o processo, escrevemos alguma entrada nele, lemos o
	// saída resultante e, finalmente, esperamos que o processo
	// para sair.
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	// Omitimos as verificações de erro no exemplo acima, mas
	// você pode usar o padrão usual `if err != nil` para
	// todos eles. Também coletamos apenas os resultados do `StdoutPipe`
	// mas você pode coletar o `StderrPipe` em
	// exatamente da mesma forma.
	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// Observe que, ao gerar comandos, precisamos
	// fornecer um comando explicitamente delineado e
	// array de argumentos, em vez de apenas poder passar um
	// string de linha de comando. Se você quiser gerar um completo
	// comando com uma string, você pode usar a opção `-c` do `bash`:
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}
```
