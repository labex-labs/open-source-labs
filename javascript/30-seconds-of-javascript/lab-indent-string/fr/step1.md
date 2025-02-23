# Une fonction pour indenter des chaînes de caractères en JavaScript

Pour ajouter une indentation à chaque ligne d'une chaîne de caractères donnée, vous pouvez utiliser la fonction `indentString()` en JavaScript. Cette fonction prend trois arguments : `str`, `count` et `indent`.

- L'argument `str` représente la chaîne de caractères que vous voulez indenter.
- L'argument `count` détermine combien de fois vous voulez indenter chaque ligne.
- L'argument `indent` est facultatif et représente le caractère que vous voulez utiliser pour l'indentation. Si vous ne le fournissez pas, la valeur par défaut est un caractère d'espace unique (`' '`).

Voici le code de la fonction `indentString()` :

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

Pour utiliser cette fonction, appelez simplement avec les arguments souhaités. Voici quelques exemples :

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

Dans le premier exemple, `indentString('Lorem\nIpsum', 2)` renvoie `'  Lorem\n  Ipsum'`, ce qui signifie que chaque ligne de la chaîne d'entrée a été indentée deux fois avec des caractères d'espace.

Dans le second exemple, `indentString('Lorem\nIpsum', 2, '_')` renvoie `'__Lorem\n__Ipsum'`, ce qui signifie que chaque ligne de la chaîne d'entrée a été indentée deux fois avec des caractères de souligné (`'_'`).
