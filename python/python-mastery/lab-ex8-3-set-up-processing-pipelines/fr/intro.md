# Introduction

**Objectifs :**

- Utiliser des coroutines pour configurer des pipelines de traitement

**Fichiers créés :** `cofollow.py`, `coticker.py`

**Note**

Pour cet exercice, le programme `stocksim.py` devrait toujours être exécuté en arrière-plan.

Dans l'exercice 8.2, vous avez écrit du code qui utilisait des générateurs pour configurer un pipeline de traitement. Un aspect clé de ce programme était l'idée de flux de données entre les fonctions génératrices. Un type de flux de données très similaire peut être configuré à l'aide de coroutines. La seule différence est que avec une coroutine, vous envoyez des données dans différents éléments de traitement, contrairement à extraire des données avec une boucle `for`.
