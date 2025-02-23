# Créer une fonction avec un contexte donné

Pour créer une fonction avec un contexte donné, utilisez la fonction `bind`. Tout d'abord, ouvrez le Terminal/SSH et tapez `node`.

La fonction `bind` crée une nouvelle fonction qui invoque la fonction d'origine avec un contexte donné. Elle peut également optionnellement ajouter tous les paramètres supplémentaires fournis aux arguments.

Pour utiliser `bind`, passez la fonction d'origine (`fn`) et le contexte souhaité (`context`). Vous pouvez également passer tout paramètre supplémentaire qui doit être lié à la fonction (`...boundArgs`).

La fonction `bind` renvoie une nouvelle fonction qui utilise `Function.prototype.apply()` pour appliquer le `context` donné à `fn`. Elle utilise également l'opérateur de propagation (`...`) pour ajouter tous les paramètres supplémentaires fournis aux arguments.

Voici un exemple d'utilisation de `bind` :

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

Dans cet exemple, nous définissons une fonction `greet` qui prend deux paramètres (`greeting` et `punctuation`) et renvoie une chaîne de caractères qui combine le `greeting`, la propriété `user` du contexte actuel (`this`) et la `punctuation`.

Nous créons ensuite un nouvel objet (`freddy`) qui a une propriété `user` définie sur `'fred'`.

Enfin, nous créons une nouvelle fonction (`freddyBound`) à l'aide de `bind`, en passant la fonction `greet` et l'objet `freddy` comme contexte souhaité. Nous pouvons ensuite appeler `freddyBound` avec deux paramètres supplémentaires (`'hi'` et `'!'`), qui sont passés à la fonction `greet` d'origine, ainsi que le contexte `freddy` lié. La sortie résultante est `'hi fred!'`.
