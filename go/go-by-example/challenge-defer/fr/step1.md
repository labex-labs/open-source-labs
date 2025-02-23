# Defer

Dans ce défi, vous devez utiliser `defer` pour créer un fichier, y écrire et ensuite le fermer une fois que vous avez fini.

## Exigences

- La fonction `createFile` doit créer un fichier avec le chemin donné et retourner un pointeur vers le fichier.
- La fonction `writeFile` doit écrire la chaîne de caractères "data" dans le fichier.
- La fonction `closeFile` doit fermer le fichier et vérifier s'il y a des erreurs.

## Exemple

```sh
# Exécution du programme confirme que le fichier est fermé
# après avoir été écrit.
$ go run defer.go
creating
writing
closing
```
