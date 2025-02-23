# Comment supprimer les balises HTML/XML d'une chaîne de caractères

Pour supprimer les balises HTML/XML d'une chaîne de caractères, vous pouvez utiliser une expression régulière. Suivez ces étapes :

1. Ouvrez le Terminal/SSH
2. Tapez `node` pour commencer à pratiquer la programmation
3. Utilisez le code suivant :

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. Testez la fonction avec l'exemple suivant :

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

Cela supprimera toutes les balises HTML/XML de la chaîne d'entrée et renverra le texte restant.
