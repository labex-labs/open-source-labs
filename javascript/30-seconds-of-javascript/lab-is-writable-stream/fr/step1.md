# Vérifier si un flux est pouvant être écrit

Pour vérifier si un flux est pouvant être écrit, ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation. Ensuite, suivez ces étapes :

1. Vérifiez si l'argument donné n'est pas `null`.
2. Utilisez `typeof` pour vérifier si la valeur est un `object` et si la propriété `pipe` est une `function`.
3. De plus, vérifiez si le `typeof` des propriétés `_write` et `_writableState` sont respectivement `function` et `object`.

Voici un exemple de code qui implémente ces vérifications :

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Vous pouvez tester cette fonction en utilisant le module `fs` dans Node.js. Par exemple :

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
