# Vérifier si un flux est lisible

Pour vérifier si un argument donné est un flux lisible, suivez ces étapes :

- Tout d'abord, ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Vérifiez si la valeur n'est pas `null`.
- Utilisez `typeof` pour vérifier si la valeur est un `objet` et si la propriété `pipe` est une `fonction`.
- De plus, vérifiez si le `typeof` des propriétés `_read` et `_readableState` sont respectivement `fonction` et `objet`.

Voici une fonction d'exemple qui met en œuvre ces étapes :

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

Vous pouvez utiliser cette fonction pour vérifier si un flux est lisible, comme ceci :

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
