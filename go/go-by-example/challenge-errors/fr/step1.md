# Erreurs

Le défi propose deux fonctions qui renvoient une erreur si l'argument d'entrée est égal à 42. La première fonction renvoie une valeur d'erreur de base, tandis que la seconde fonction utilise un type personnalisé pour représenter l'erreur.

## Exigences

- Le package `errors` doit être importé.
- La fonction `f1` doit renvoyer une erreur si l'argument d'entrée est égal à 42.
- La fonction `f2` doit renvoyer une erreur de type `argError` si l'argument d'entrée est égal à 42.
- Le type `argError` doit avoir deux champs : `arg` et `prob`.
- Le type `argError` doit implémenter la méthode `Error()`.
- La fonction `main` doit appeler à la fois `f1` et `f2` avec des arguments d'entrée de 7 et 42.
- La fonction `main` doit afficher le résultat de chaque appel de fonction, ainsi que toute erreur qui a été renvoyée.
- La fonction `main` doit démontrer comment utiliser programmatiquement les données dans une erreur personnalisée.

## Exemple

```sh
$ go run errors.go
f1 a fonctionné : 10
f1 a échoué : impossible de travailler avec 42
f2 a fonctionné : 10
f2 a échoué : 42 - impossible de travailler avec
42
impossible de travailler avec

# Consultez cet excellent article [ici](https://go.dev/blog/error-handling-and-go)
# sur le blog Go pour en savoir plus sur la gestion des erreurs.
```
