# Interfaces

Le problème est d'implémenter une interface en Go, il suffit d'implémenter toutes les méthodes de l'interface. Ici, on implémente `geometry` pour les `rect` et les `circle`.

## Exigences

- Implémenter une interface en Go.
- Implémenter toutes les méthodes de l'interface.
- Utiliser une fonction générique `measure` pour travailler sur n'importe quelle `geometry`.
- Utiliser des instances des structs `circle` et `rect` comme arguments pour `measure`.

## Exemple

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Pour en savoir plus sur les interfaces de Go, consultez ce
# [super article de blog](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```
