# Currying d'une fonction

Pour effectuer le currying d'une fonction, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage.
2. Utilisez la récursivité.
3. Vérifiez si le nombre d'arguments fournis (`args`) est suffisant.
4. Si c'est le cas, appelez la fonction passée `fn`.
5. Si ce n'est pas le cas, utilisez `Function.prototype.bind()` pour retourner une fonction curryée `fn` qui attend le reste des arguments.
6. Si vous voulez effectuer le currying d'une fonction qui accepte un nombre variable d'arguments (une fonction variadique, par exemple `Math.min()`), vous pouvez optionnellement passer le nombre d'arguments au deuxième paramètre `arity`.
7. Utilisez le code suivant :

```js
const curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

Voici quelques exemples :

```js
curry(Math.pow)(2)(10); // 1024
curry(Math.min, 3)(10)(50)(2); // 2
```
