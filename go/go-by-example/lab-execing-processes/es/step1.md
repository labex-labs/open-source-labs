# Ejecución de procesos

El problema consiste en reemplazar el proceso actual de Go con otro proceso, como un proceso no escrito en Go.

- Lenguaje de programación Go
- Conocimientos básicos de la función `exec` de Go
- Familiaridad con las variables de entorno

```sh
# Cuando ejecutamos nuestro programa, es reemplazado por `ls`.
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# Tenga en cuenta que Go no ofrece una función `fork` clásica de Unix.
# Por lo general, esto no es un problema, ya que iniciar gorutinas,
# crear procesos y ejecutar procesos cubre la mayoría de los casos de uso de `fork`.
```

A continuación se muestra el código completo:

```go
// En el ejemplo anterior, vimos cómo [crear procesos externos](spawning-processes).
// Hacemos esto cuando necesitamos un proceso externo accesible para un proceso de Go en ejecución.
// A veces simplemente queremos reemplazar completamente el proceso actual de Go con otro (quizás no escrito en Go).
// Para hacer esto, usaremos la implementación de Go de la clásica función <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>.

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// Para nuestro ejemplo, ejecutaremos `ls`. Go requiere una ruta absoluta al binario que queremos ejecutar,
	// por lo que usaremos `exec.LookPath` para encontrarlo (probablemente `/bin/ls`).
	binary, lookErr := exec.LookPath("ls")
	if lookErr!= nil {
		panic(lookErr)
	}

	// `Exec` requiere los argumentos en forma de slice (en lugar de una gran cadena).
	// Le daremos a `ls` algunos argumentos comunes. Tenga en cuenta que el primer argumento debe ser el nombre del programa.
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` también necesita un conjunto de [variables de entorno](environment-variables) para usar.
	// Aquí simplemente proporcionamos nuestro entorno actual.
	env := os.Environ()

	// Aquí está la llamada real a `syscall.Exec`. Si esta llamada es exitosa, la ejecución de nuestro proceso terminará aquí
	// y será reemplazado por el proceso `/bin/ls -a -l -h`. Si hay un error, obtendremos un valor de retorno.
	execErr := syscall.Exec(binary, args, env)
	if execErr!= nil {
		panic(execErr)
	}
}

```
