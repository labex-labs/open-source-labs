# Vérifier si les arguments de processus contiennent des drapeaux

Pour vérifier si les arguments du processus actuel contiennent des drapeaux spécifiés, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.every()` et `Array.prototype.includes()` pour vérifier si `process.argv` contient tous les drapeaux spécifiés.
3. Utilisez une expression régulière pour tester si les drapeaux spécifiés sont préfixés avec `-` ou `--` et les préfixer en conséquence.

Voici un extrait de code qui montre comment implémenter cela :

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag)
  );
```

Vous pouvez tester la fonction avec différents drapeaux comme ceci :

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
