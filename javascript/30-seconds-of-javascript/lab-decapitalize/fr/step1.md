# Fonction JavaScript pour décapitaliser une chaîne de caractères

Pour décapitaliser la première lettre d'une chaîne de caractères, utilisez la fonction JavaScript suivante :

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

Pour utiliser cette fonction, ouvrez le Terminal/SSH et tapez `node`. Ensuite, appelez la fonction `decapitalize`, en passant en premier argument la chaîne de caractères que vous voulez décapitaliser.

Facultativement, vous pouvez définir le deuxième argument `upperRest` sur `true` pour convertir le reste de la chaîne en majuscules. Si `upperRest` n'est pas fourni, il prend la valeur par défaut `false`.

Voici quelques exemples :

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
