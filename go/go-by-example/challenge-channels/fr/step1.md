# Canaux

Dans ce défi, vous devrez créer un nouveau canal et y envoyer une valeur à partir d'une nouvelle goroutine. Vous devrez ensuite recevoir la valeur du canal et l'afficher.

## Exigences

- Vous devez utiliser la syntaxe `make(chan val-type)` pour créer un nouveau canal.
- Le canal doit être typé par les valeurs qu'il transporte.
- Vous devez utiliser la syntaxe `channel <-` pour envoyer une valeur dans le canal.
- Vous devez utiliser la syntaxe `<-channel` pour recevoir une valeur du canal.
- Vous devez utiliser une nouvelle goroutine pour envoyer la valeur dans le canal.

## Exemple

```sh
# Lorsque nous exécutons le programme, le message `"ping"` est
# correctement transmis d'une goroutine à l'autre via
# notre canal.
$ go run channels.go
ping

# Par défaut, les envois et les réceptions bloquent jusqu'à ce que
# l'expéditeur et le destinataire soient prêts. Cette propriété nous a
# permis d'attendre à la fin de notre programme le message `"ping"`
# sans avoir à utiliser d'autres méthodes de synchronisation.
```
