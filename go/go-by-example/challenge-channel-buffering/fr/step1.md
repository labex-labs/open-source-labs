# Channel Buffering

Par défaut, les canaux en Golang sont non tamponnés, ce qui signifie qu'ils n'acceptent des envois que s'il existe une réception correspondante prête à recevoir la valeur envoyée. Cependant, les canaux tamponnés acceptent un nombre limité de valeurs sans récepteur correspondant pour ces valeurs. Dans ce défi, vous êtes requis de créer un canal tamponné et d'envoyer des valeurs dans le canal sans réception concurrente correspondante.

## Exigences

- Connaissance de base des canaux en Golang
- Compréhension des canaux tamponnés

## Exemple

```sh
$ go run channel-buffering.go
buffered
channel
```
