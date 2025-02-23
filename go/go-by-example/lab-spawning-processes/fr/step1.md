# Démarrage de processus

Le laboratoire nécessite la mise en œuvre d'un programme Go qui démarre des processus externes et collecte leur sortie.

- Le programme doit être capable de démarrer des processus externes.
- Le programme doit être capable de collecter la sortie des processus externes.
- Le programme doit gérer les erreurs qui peuvent survenir pendant l'exécution des processus externes.

```sh
# Les programmes démarrés renvoient une sortie identique
# à celle que nous obtiendrions si nous les avions exécutés
# directement à partir de la ligne de commande.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date n'a pas de drapeau `-x`, donc il se terminera
# avec un message d'erreur et un code de retour non nul.
commande terminée avec rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```

Voici le code complet ci-dessous :

```go
// Parfois, nos programmes Go doivent démarrer d'autres processus,
// non-Go.

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {

	// Nous commencerons par une commande simple qui ne prend
	// aucun argument ni entrée et qui n'affiche que quelque
	// chose sur la sortie standard. La fonction utilitaire
	// `exec.Command` crée un objet pour représenter ce
	// processus externe.
	dateCmd := exec.Command("date")

	// La méthode `Output` exécute la commande, attend qu'elle
	// se termine et collecte sa sortie standard.
	// Si aucune erreur n'est survenue, `dateOut` contiendra
	// les bytes de l'information de date.
	dateOut, err := dateCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// `Output` et les autres méthodes de `Command` renverront
	// `*exec.Error` s'il y a eu un problème lors de
	// l'exécution de la commande (par exemple, mauvais chemin),
	// et `*exec.ExitError` si la commande s'est exécutée
	// mais s'est terminée avec un code de retour non nul.
	_, err = exec.Command("date", "-x").Output()
	if err!= nil {
		switch e := err.(type) {
		case *exec.Error:
			fmt.Println("échec de l'exécution :", err)
		case *exec.ExitError:
			fmt.Println("code de sortie de la commande =", e.ExitCode())
		default:
			panic(err)
		}
	}

	// Ensuite, nous examinerons un cas un peu plus complexe
	// où nous envoyons des données à l'entrée standard du
	// processus externe et collectons les résultats de sa
	// sortie standard.
	grepCmd := exec.Command("grep", "hello")

	// Ici, nous récupérons explicitement les tubes
	// d'entrée/sortie, démarrons le processus, écrivons
	// quelques données dans son entrée, lisons la sortie
	// résultante et, finalement, attendons que le processus
	// se termine.
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	// Nous avons omis les vérifications d'erreur dans
	// l'exemple ci-dessus, mais vous pouvez utiliser le
	// modèle habituel `if err!= nil` pour toutes les
	// opérations. Nous ne collectons également que les
	// résultats du `StdoutPipe`, mais vous pouvez
	// collecter les résultats du `StderrPipe` exactement
	// de la même manière.
	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// Notez que lorsqu'on démarre des commandes, il faut
	// fournir un tableau de commande et d'arguments
	// explicitement délimité, contrairement à la possibilité
	// de simplement passer une chaîne de commande unique.
	// Si vous voulez exécuter une commande complète avec
	// une chaîne, vous pouvez utiliser l'option `-c` de
	// `bash` :
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}

```
