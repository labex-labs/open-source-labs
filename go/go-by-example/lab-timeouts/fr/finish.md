# Summary

Dans ce laboratoire, nous avons appris comment implémenter des délais d'attente en Go à l'aide de canaux et de `select`. Nous avons utilisé un canal tamponné pour éviter les fuites de goroutine au cas où le canal n'est jamais lu, et `time.After` pour attendre qu'une valeur soit envoyée après le délai d'attente. Nous avons également utilisé `select` pour passer à la première réception prête.
