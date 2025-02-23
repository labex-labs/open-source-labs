# Opérations non bloquantes sur les canaux

Le problème à résoudre dans ce défi est d'implémenter des opérations non bloquantes sur les canaux en utilisant l'instruction `select` avec une clause `default`.

## Exigences

- Implémentez une réception non bloquante sur un canal en utilisant l'instruction `select` avec une clause `default`.
- Implémentez un envoi non bloquante sur un canal en utilisant l'instruction `select` avec une clause `default`.
- Implémentez une sélection multi-voie non bloquante en utilisant l'instruction `select` avec plusieurs clauses `case` et une clause `default`.

## Exemple

```sh
$ go run non-blocking-channel-operations.go
aucun message reçu
aucun message envoyé
aucune activité
```
