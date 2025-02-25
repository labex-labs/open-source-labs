# File d'attente prioritaire

## Problème

Implémentez une file d'attente prioritaire supportée par un tableau. La file d'attente prioritaire devrait prendre en charge les méthodes suivantes :

- `insert` : insère un nouvel élément dans la file d'attente prioritaire
- `extract_min` : supprime et renvoie l'élément minimum de la file d'attente prioritaire
- `decrease_key` : diminue la clé d'un élément donné dans la file d'attente prioritaire

## Exigences

Pour implémenter la file d'attente prioritaire, nous devons répondre aux exigences suivantes :

- Les méthodes prises en charge par la file d'attente prioritaire devraient être `insert`, `extract_min` et `decrease_key`.
- Il n'y aura pas de clés dupliquées dans la file d'attente prioritaire.
- Nous n'avons pas besoin de valider les entrées.
- La file d'attente prioritaire devrait tenir en mémoire.

## Utilisation de l'exemple

Voici quelques exemples d'utilisation des méthodes de la file d'attente prioritaire :

### insert

- Cas général de `insert` : insère un nouveau nœud dans la file d'attente prioritaire.

### extract_min

- `extract_min` à partir d'une liste vide : renvoie None.
- Cas général de `extract_min` : supprime et renvoie le nœud minimum de la file d'attente prioritaire.

### decrease_key

- `decrease_key` avec une clé invalide : renvoie None.
- Cas général de `decrease_key` : diminue la clé d'un nœud donné dans la file d'attente prioritaire.
