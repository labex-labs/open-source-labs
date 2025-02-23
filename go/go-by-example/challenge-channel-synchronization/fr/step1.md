# Synchronisation par canal

Le problème à résoudre dans ce défi est de créer une goroutine qui effectue un certain travail et qui avertit une autre goroutine lorsqu'elle a terminé, en utilisant un canal.

## Exigences

Pour résoudre ce défi, vous devrez :

- Créer une fonction nommée `worker` qui prend en paramètre un canal de type `bool`.
- Dans la fonction `worker`, effectuer un certain travail puis envoyer une valeur au canal pour signaler que le travail est terminé.
- Dans la fonction `main`, créer un canal de type `bool` avec une taille de tampon de 1.
- Démarrer une goroutine qui appelle la fonction `worker` et passe le canal en paramètre.
- Bloquer la fonction `main` jusqu'à ce qu'une valeur soit reçue du canal.

## Exemple

```sh
$ go run channel-synchronization.go
working...done

# Si vous retirez la ligne `<- done` de ce programme, le
# programme se terminera avant que le `worker` ait même
# commencé.
```
