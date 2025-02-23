# Timeouts

Lorsque les programmes se connectent à des ressources externes ou ont besoin de limiter le temps d'exécution, les délais d'attente sont importants. Le défi est de mettre en œuvre des délais d'attente en Go à l'aide de canaux et de `select`.

## Exigences

- Mettre en œuvre des délais d'attente en Go à l'aide de canaux et de `select`.
- Utiliser un canal tamponné pour éviter les fuites de goroutine au cas où le canal n'est jamais lu.
- Utiliser `time.After` pour attendre qu'une valeur soit envoyée après le délai d'attente.
- Utiliser `select` pour passer à la première réception prête.

## Exemple

```sh
# Exécution de ce programme montre que la première opération
# atteint le délai d'attente et que la seconde réussit.
$ go run timeouts.go
timeout 1
result 2
```
