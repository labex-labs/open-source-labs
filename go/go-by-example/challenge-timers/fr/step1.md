# Timers

Le défi consiste à implémenter un timer qui attend une durée spécifiée puis déclenche une action. De plus, le timer doit être annulable avant son déclenchement.

## Exigences

- Le package `time` doit être importé.
- Deux timers doivent être créés, l'un qui attend 2 secondes et l'autre qui attend 1 seconde.
- Le premier timer doit afficher "Timer 1 fired" lorsqu'il déclenche.
- Le second timer doit afficher "Timer 2 fired" lorsqu'il déclenche.
- Le second timer doit être annulé avant son déclenchement.
- Le programme doit attendre 2 secondes pour montrer que le second timer n'a pas déclenché.

## Exemple

```sh
// Le premier timer déclenchera ~2s après le lancement
// du programme, mais le second devrait être arrêté avant
// qu'il ait le temps de déclencher.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```
