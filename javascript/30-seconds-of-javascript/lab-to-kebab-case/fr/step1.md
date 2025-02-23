# Conversion d'une chaîne en kebab case

Pour convertir une chaîne en kebab case, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.match()` pour diviser la chaîne en mots à l'aide d'une expression régulière appropriée.
3. Utilisez `Array.prototype.map()`, `Array.prototype.join()` et `String.prototype.toLowerCase()` pour combiner les mots, en ajoutant ` -` comme séparateur.

Voici une fonction d'exemple qui effectue la conversion :

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

Vous pouvez utiliser cette fonction pour convertir des chaînes en kebab case comme indiqué ci-dessous :

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); //'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
//'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
