# Fonction pour convertir une chaîne en snake case

Pour convertir une chaîne en snake case, utilisez la fonction suivante :

```js
const toSnakeCase = (str) => {
  if (!str) return "";
  const regex =
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
  return str
    .match(regex)
    .map((x) => x.toLowerCase())
    .join("_");
};
```

Cette fonction utilise `String.prototype.match()` pour découper la chaîne en mots en utilisant une expression régulière appropriée. Ensuite, elle utilise `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` et `String.prototype.toLowerCase()` pour combiner les mots, en ajoutant `_` comme séparateur.

Utilisation exemple :

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); //'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
//'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
