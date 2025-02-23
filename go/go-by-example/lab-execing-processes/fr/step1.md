# Executing des processus

Le problème est de remplacer le processus Go actuel par un autre processus, tel qu'un processus non-Go.

- Langage de programmation Go
- Connaissance de base de la fonction `exec` de Go
- Familiarité avec les variables d'environnement

```sh
# Lorsque nous exécutons notre programme, il est remplacé par `ls`.
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# Notez que Go ne propose pas une fonction `fork` classique Unix.
# Généralement, cela n'est pas un problème, car démarrer des goroutines,
# lancer des processus et exécuter des processus couvre la plupart des
# cas d'utilisation de `fork`.
```

Voici le code complet ci-dessous :

```go
// Dans l'exemple précédent, nous avons examiné
// [lancement de processus externes](spawning-processes). Nous le
// faisons lorsque nous avons besoin d'un processus externe accessible
// à un processus Go en cours d'exécution. Parfois, nous voulons simplement
// remplacer complètement le processus Go actuel par un autre (peut-être
// non-Go). Pour ce faire, nous utiliserons l'implémentation Go de la
// classique <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>
// fonction.

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// Pour notre exemple, nous allons exécuter `ls`. Go nécessite un
	// chemin absolu vers le binaire que nous voulons exécuter, donc
	// nous utiliserons `exec.LookPath` pour le trouver (probablement
	// `/bin/ls`).
	binary, lookErr := exec.LookPath("ls")
	if lookErr!= nil {
		panic(lookErr)
	}

	// `Exec` nécessite des arguments au format de slice (au
	// contraire d'une grande chaîne de caractères). Nous donnerons à `ls`
	// quelques arguments courants. Notez que le premier argument devrait
	// être le nom du programme.
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` a également besoin d'un ensemble de [variables d'environnement](environment-variables)
	// à utiliser. Ici, nous fournissons simplement notre environnement
	// actuel.
	env := os.Environ()

	// Voici l'appel réel à `syscall.Exec`. Si cet appel est
	// réussi, l'exécution de notre processus se terminera ici et sera
	// remplacée par le processus `/bin/ls -a -l -h`. S'il y a une erreur,
	// nous obtiendrons une valeur de retour.
	execErr := syscall.Exec(binary, args, env)
	if execErr!= nil {
		panic(execErr)
	}
}

```
