# Comment obtenir le nom d'une fonction en JavaScript

Pour obtenir le nom d'une fonction JavaScript, suivez ces étapes :

1. Ouvrez le Terminal ou SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Utilisez `console.debug()` et la propriété `name` de la fonction passée pour afficher le nom de la fonction dans la chaîne `debug` de la console.
4. Retournez la fonction donnée `fn`.

Voici un extrait de code d'exemple qui montre comment obtenir le nom d'une fonction en JavaScript :

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// Le nom de la fonction'max' est affiché dans la chaîne debug de la console.
// m = 6
```

Dans cet exemple, la fonction `functionName` affiche le nom de la fonction passée dans la chaîne `debug` de la console et retourne la fonction elle-même. La propriété `name` de la fonction est utilisée pour obtenir son nom.
