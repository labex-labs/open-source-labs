# Introduction

**Objectifs :**

- Découvrir les générateurs gérés

**Fichiers créés :** `multitask.py`, `server.py`

Une fonction génératrice ou une coroutine ne peut jamais s'exécuter sans être entraînée par un autre code. Par exemple, un générateur utilisé pour l'itération ne fait rien tant qu'aucune itération n'est effectivement effectuée à l'aide d'une boucle `for`. De même, une collection de coroutines ne s'exécutera pas à moins que sa méthode `send()` ne soit invoquée d'une certaine manière.

Dans les applications avancées des générateurs, il est possible d'entraîner les générateurs de diverses manières inhabituelles. Dans cet exercice, nous examinons quelques exemples.
