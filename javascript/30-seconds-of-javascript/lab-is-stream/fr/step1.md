# Comment vérifier si une valeur est un flux en Node.js

Pour vérifier si une valeur est un flux en Node.js, vous pouvez utiliser la fonction `isStream`. Pour utiliser cette fonction, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Utilisez la fonction `isStream` pour vérifier si l'argument donné est un flux.
4. Pour vérifier si la valeur est différente de `null`, utilisez le code suivant :

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. Pour vérifier si un fichier est un flux, utilisez le code suivant :

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
