# Décodage d'une chaîne encodée en base64

Pour décoder une chaîne de données qui a été encodée en utilisant l'encodage base-64, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez un `Buffer` pour la chaîne donnée avec l'encodage base-64.
3. Utilisez `Buffer.prototype.toString()` pour retourner la chaîne décodée.

Voici un extrait de code d'exemple :

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

Vous pouvez tester cette fonction en exécutant `atob('Zm9vYmFy')` qui devrait retourner `'foobar'`.
