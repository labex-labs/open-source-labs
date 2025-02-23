# Comment tronquer une chaîne de caractères à l'espace dans JavaScript

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici une fonction qui tronque une chaîne de caractères jusqu'à une longueur spécifiée tout en respectant les espaces le plus possible :

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

Pour utiliser cette fonction, passez la chaîne de caractères que vous voulez tronquer en tant que premier argument, la longueur maximale en tant que deuxième argument et une chaîne de caractères de fin optionnelle en tant que troisième argument. Si la longueur de la chaîne est inférieure ou égale à la limite spécifiée, la chaîne d'origine sera renvoyée. Sinon, la fonction trouvera le dernier espace avant la limite et tronquera la chaîne à ce point, en ajoutant la chaîne de fin si elle est spécifiée.

Voici quelques exemples :

```js
truncateStringAtWhitespace("short", 10); // 'court'
truncateStringAtWhitespace("pas si court", 10); // 'pas si...'
truncateStringAtWhitespace("essayer une chose", 10); // 'essayer...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
