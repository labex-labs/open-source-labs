# Une fonction qui appelle ou renvoie une autre fonction

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici une fonction appelée `callOrReturn` qui prend un argument et l'appelle s'il s'agit d'une fonction, sinon, elle le renvoie. Voici comment elle fonctionne :

- La fonction prend deux paramètres : `fn` et `...args`. `fn` est l'argument à vérifier, et `...args` est la liste d'arguments à passer à la fonction s'il est appelé.
- Elle utilise l'opérateur `typeof` pour vérifier si l'argument donné est une fonction.
- Si l'argument est effectivement une fonction, elle appelle la fonction en utilisant l'opérateur de propagation (`...`) pour passer le reste des arguments donnés. Sinon, elle renvoie simplement l'argument.
- Voici un exemple d'utilisation de la fonction `callOrReturn` :

```js
const callOrReturn = (fn, ...args) =>
  typeof fn === "function" ? fn(...args) : fn;

callOrReturn((x) => x + 1, 1); // 2
callOrReturn(1, 1); // 1
```

Dans le premier exemple, `callOrReturn(x => x + 1, 1)` appelle la fonction `x => x + 1` avec l'argument `1`, qui renvoie `2`. Dans le second exemple, `callOrReturn(1, 1)` renvoie simplement `1` car ce n'est pas une fonction.
