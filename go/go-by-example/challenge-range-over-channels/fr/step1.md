# Range sur des canaux

Vous êtes requis d'écrire une fonction qui prend un canal d'entiers et renvoie la somme de tous les entiers reçus à partir du canal.

## Exigences

- La fonction doit s'appeler `sumInts`.
- La fonction doit prendre un seul paramètre de type `chan int`.
- La fonction doit renvoyer une seule valeur entière.
- Il n'est pas autorisé d'utiliser de boucles ou de récursion à l'intérieur du corps de la fonction.
- Il n'est pas autorisé d'utiliser de packages externes.

## Exemple

```sh
$ go run range-over-channels.go
one
two

# Cet exemple a également montré qu'il est possible de fermer
# un canal non vide mais de recevoir encore les valeurs restantes.
```
