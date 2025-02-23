# Fonction pour tester si tous les éléments d'un tableau sont considérés comme "faux" (falsy)

Pour tester si tous les éléments d'un tableau sont considérés comme "faux" (falsy), suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.some()` pour tester si un ou plusieurs éléments de la collection renvoient `true` en fonction de la fonction prédicat fournie.
3. Si vous omettez le deuxième argument, `fn`, la fonction utilisera `Boolean` comme valeur par défaut.
4. La fonction renvoie `true` si tous les éléments du tableau sont considérés comme "faux" (falsy), et `false` sinon.

Voici une implémentation de l'exemple de la fonction :

```js
const none = (arr, fn = Boolean) => !arr.some(fn);
```

Vous pouvez utiliser la fonction comme suit :

```js
none([0, 1, 3, 0], (x) => x == 2); // true
none([0, 0, 0]); // true
```
