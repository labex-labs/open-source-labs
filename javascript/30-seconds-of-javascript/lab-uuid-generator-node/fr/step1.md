# Générer un UUID en Node.js

Pour générer un UUID en Node.js, suivez les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `crypto.randomBytes()` pour générer un UUID conforme à la version 4 de la [RFC4122](https://www.ietf.org/rfc/rfc4122.txt).
3. Convertissez le UUID généré en une chaîne hexadécimale valide en utilisant la méthode `Number.prototype.toString()`.
4. Alternativement, vous pouvez utiliser la méthode [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions) qui offre une fonctionnalité similaire.

Voici un extrait de code d'exemple pour générer un UUID en Node.js :

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

Vous pouvez appeler la méthode `UUIDGeneratorNode()` pour générer un UUID.

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
