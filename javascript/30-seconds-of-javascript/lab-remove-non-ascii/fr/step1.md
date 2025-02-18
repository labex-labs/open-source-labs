# Comment supprimer les caractères non ASCII en JavaScript

Pour supprimer les caractères ASCII non imprimables en JavaScript, vous pouvez suivre ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage.
2. Utilisez la méthode `String.prototype.replace()` avec une expression régulière pour supprimer les caractères ASCII non imprimables.
3. L'expression régulière `/[^\x20-\x7E]/g` correspond à tout caractère qui n'est pas dans la plage ASCII imprimable (valeurs décimales de 32 à 126).
4. Le marqueur `g` est utilisé pour effectuer une correspondance globale (c'est-à-dire remplacer toutes les occurrences de caractères non ASCII dans la chaîne).
5. Voici un exemple de comment utiliser la fonction `removeNonASCII` :

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

Cela renverra la chaîne avec tous les caractères non ASCII supprimés.
