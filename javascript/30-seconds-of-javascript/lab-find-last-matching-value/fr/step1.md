# Fonction JavaScript pour Trouver la Dernière Valeur Correspondante

Pour trouver le dernier élément d'un tableau qui satisfait une condition donnée, utilisez la fonction JavaScript suivante :

```js
const findLast = (arr, fn) => arr.filter(fn).pop();
```

Pour utiliser cette fonction, passez le tableau que vous voulez rechercher et une fonction qui renvoie une valeur véridique pour les éléments que vous voulez correspondre.

Par exemple, `findLast([1, 2, 3, 4], n => n % 2 === 1);` renverra `3`, car il trouve le dernier nombre impair dans le tableau.

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
