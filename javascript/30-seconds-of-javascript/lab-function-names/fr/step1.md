# Comment obtenir les noms de propriétés de fonction à partir d'un objet en JavaScript

Pour obtenir un tableau des noms de propriétés de fonction à partir d'un objet, utilisez la fonction `functions` fournie ci-dessous. Cette fonction peut également inclure facultativement les propriétés héritées.

Voici comment utiliser la fonction `functions` :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.keys()` pour itérer sur les propriétés propres à l'objet.
3. Si vous voulez inclure les propriétés héritées, définissez l'argument `inherited` sur `true` et utilisez `Object.getPrototypeOf()` pour obtenir les propriétés héritées de l'objet.
4. Utilisez `Array.prototype.filter()` pour ne conserver que les propriétés qui sont des fonctions.
5. Omettez le second argument, `inherited`, pour ne pas inclure les propriétés héritées par défaut.

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

Voici un exemple d'utilisation de la fonction `functions` :

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
