# Utilisation des expressions régulières pour la division en mots

Pour convertir une chaîne de caractères en casse Pascal (Pascal case), la première étape consiste à diviser la chaîne en mots individuels. Nous pouvons utiliser des expressions régulières (regex) pour identifier les limites des mots, quelle que soit le délimiteur utilisé (espaces, tirets, underscores, etc.).

En JavaScript, les expressions régulières sont encadrées par des barres obliques (`/motif/`). Explorons comment utiliser les regex pour diviser une chaîne de caractères en mots.

1. Dans votre session Node.js, essayons d'abord un exemple simple. Tapez le code suivant :

```javascript
let str = "hello_world-example";
let words = str.split(/[-_]/);
console.log(words);
```

La sortie devrait être :

```
[ 'hello', 'world', 'example' ]
```

Cette regex `/[-_]/` correspond soit à un tiret, soit à un underscore, et `split()` utilise ces correspondances comme séparateurs.

2. Maintenant, essayons une chaîne de caractères et une regex plus complexes. Tapez :

```javascript
let complexStr = "hello_WORLD-example phrase";
let regex =
  /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
let matches = complexStr.match(regex);
console.log(matches);
```

La sortie devrait être :

```
[ 'hello', 'WORLD', 'example', 'phrase' ]
```

Décortiquons cette regex :

- `/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)/` : Correspond aux séquences de lettres majuscules
- `/[A-Z]?[a-z]+[0-9]*/` : Correspond aux mots qui peuvent commencer par une lettre majuscule
- `/[A-Z]/` : Correspond aux lettres majuscules isolées
- `/[0-9]+/` : Correspond aux séquences de nombres
- Le marqueur `g` rend la correspondance globale (trouve toutes les correspondances)

La méthode `match()` renvoie un tableau de toutes les correspondances trouvées dans la chaîne de caractères. Cela sera essentiel pour notre convertisseur en casse Pascal, car il peut identifier les mots dans presque n'importe quel format.
