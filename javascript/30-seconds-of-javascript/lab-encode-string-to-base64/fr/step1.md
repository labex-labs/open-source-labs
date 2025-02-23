# Encodage d'une chaîne en Base64

Pour encoder un objet String en une chaîne ASCII encodée en Base64, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.
2. Créez un `Buffer` à l'aide de la chaîne donnée et du codage binaire.
3. Utilisez `Buffer.prototype.toString()` pour renvoyer la chaîne encodée en Base64.

Voici un extrait de code d'exemple :

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

Vous pouvez maintenant utiliser la fonction `encodeToBase64()` pour encoder n'importe quelle chaîne en Base64. Par exemple :

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
