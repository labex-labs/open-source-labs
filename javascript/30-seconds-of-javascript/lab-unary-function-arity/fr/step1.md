# Comprendre l'arity des fonctions unaire

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

L'arity d'une fonction unaire désigne une fonction qui prend seulement un argument, en ignorant tout argument supplémentaire.

La fonction fournie `fn` peut être appelée avec seulement le premier argument fourni. Pour créer une fonction unaire, utilisez le code suivant :

```js
const unary = (fn) => (val) => fn(val);
```

Un exemple d'utilisation de `unary` avec la fonction `parseInt` est montré ci-dessous :

```js
["6", "8", "10"].map(unary(parseInt)); // [6, 8, 10]
```
