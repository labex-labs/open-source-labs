# Comment comparer les propriétés d'objets en JavaScript

Pour comparer deux objets et vérifier s'ils ont les mêmes valeurs de propriété, utilisez la fonction `matches`. Voici comment l'utiliser :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.
2. Copiez et collez le code de la fonction `matches` dans votre fichier JavaScript.
3. Appelez la fonction et passez deux objets en arguments. Le premier objet est celui que vous voulez comparer, et le second objet est celui avec lequel vous voulez le comparer.

```js
matches({ age: 25, hair: "long", beard: true }, { hair: "long", beard: true });
// true
matches({ hair: "long", beard: true }, { age: 25, hair: "long", beard: true });
// false
```

La fonction `matches` utilise `Object.keys()` pour obtenir toutes les clés du second objet puis vérifie si toutes les clés existent dans le premier objet et ont les mêmes valeurs en utilisant `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` et une comparaison stricte.
