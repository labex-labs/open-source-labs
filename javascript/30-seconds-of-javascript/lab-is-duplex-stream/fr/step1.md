# Vérifier si un flux est duplex

Pour vérifier si un flux est duplex (lisible et écrivable), ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation. Ensuite, suivez ces étapes :

1. Vérifiez si l'argument donné est différent de `null`.
2. Utilisez `typeof` pour vérifier si l'argument donné est de type `object` et s'il a une propriété `pipe` de type `function`.
3. De plus, vérifiez si les propriétés `_read`, `_write`, `_readableState` et `_writableState` sont respectivement de type `function` et `object`.

Voici le code :

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Vous pouvez tester ce code à l'aide de l'exemple suivant :

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
