# Fonction pour Combiner des Tableaux avec une Fonction de Mappage Fournie

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction renvoie un tableau d'éléments qui existent dans l'un ou l'autre des deux tableaux d'entrée, après avoir appliqué la fonction de mappage fournie à chaque élément des deux tableaux.

Voici les étapes pour y arriver :

1. Créez un nouveau `Set` en appliquant la fonction de mappage à toutes les valeurs du premier tableau d'entrée `a`.
2. Créez un autre `Set` constitué de tous les éléments de `b` qui ne correspondent à aucune valeur du `Set` précédemment créé lorsqu'on applique la fonction de mappage.
3. Combinez les deux ensembles et convertissez-les en un tableau.
4. Retournez le tableau résultant.

Voici le code pour la fonction `unionBy` :

```js
const unionBy = (a, b, fn) => {
  const setA = new Set(a.map(fn));
  return Array.from(new Set([...a, ...b.filter((x) => !setA.has(fn(x)))]));
};
```

Voici quelques exemples d'utilisation de la fonction `unionBy` :

```js
unionBy([2.1], [1.2, 2.3], Math.floor); // Sortie : [2.1, 1.2]
unionBy([{ id: 1 }, { id: 2 }], [{ id: 2 }, { id: 3 }], (x) => x.id);
// Sortie : [{ id: 1 }, { id: 2 }, { id: 3 }]
```
