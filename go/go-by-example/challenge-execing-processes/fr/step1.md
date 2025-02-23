# Executing des processus

Le problème est de remplacer le processus Go actuel par un autre processus, tel qu'un processus non-Go.

## Exigences

- Langage de programmation Go
- Connaissance de base de la fonction `exec` de Go
- Familiarité avec les variables d'environnement

## Exemple

```sh
# Lorsque nous exécutons notre programme, il est remplacé par `ls`.
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# Notez que Go ne propose pas une fonction `fork` classique Unix.
# Généralement, cela n'est pas un problème, car démarrer des goroutines,
# créer des processus et exécuter des processus couvre la plupart
# des cas d'utilisation de `fork`.
```
